#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🎓 HUAWEI HCIA-AI V4.0 (H13-311_V4.0) • OFFICIAL INTERACTIVE EXAM SIMULATOR
Authentic Pearson VUE Testing Environment • 60 Questions • 1000 Points • 90 Minutes
Integrates BOTH Moderate & Hard/Tricky Levels into One Single Comprehensive Exam
Curated by: Umed Jamal Nouri • Release v1.3.0
================================================================================
"""

import sys
import os
import json
import random
import time
from datetime import datetime

# Configure UTF-8 for console output
try:
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# ANSI Color Codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# Enable Windows terminal ANSI colors
if os.name == 'nt' and not os.environ.get('WT_SESSION') and not os.environ.get('ANSICON'):
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

def cprint(text, color=Colors.RESET, bold=False, end='\n'):
    prefix = Colors.BOLD if bold else ''
    print(f"{prefix}{color}{text}{Colors.RESET}", end=end)

# Load Database
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '02_Question_Banks', 'data', 'exam_database.json')

def load_database():
    if not os.path.exists(DB_PATH):
        cprint(f"Error: Question database not found at {DB_PATH}", Colors.RED, bold=True)
        sys.exit(1)
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def normalize_answer(ans_str):
    """Normalize answer string to sorted uppercase letters e.g. 'a, c' -> 'AC', 'true' -> 'A'"""
    if not ans_str:
        return ""
    cleaned = ans_str.upper().strip()
    if cleaned in ['TRUE', 'T']:
        return 'A'
    if cleaned in ['FALSE', 'F']:
        return 'B'
    chars = [c for c in cleaned if c in 'ABCD']
    return "".join(sorted(list(set(chars))))

def select_exam_questions(all_questions, mode):
    """
    Selects and randomizes questions based on chosen mode:
    1: Comprehensive Real Exam (Combines BOTH Moderate & Hard/Tricky in ONE exam - 60Q)
    2: Real Exam Recall Drill (Authentic test-taker recall - 60Q)
    3: Quick Practice Sprint (Mixed Moderate & Tricky - 15Q)
    """
    selected = []
    
    if mode == 1:
        # UNIFIED COMPREHENSIVE EXAM: Integrates both Moderate & Hard/Tricky in ONE exam!
        # 30 Moderate questions (core definitions & standard concepts)
        # 30 Hard & Tricky questions (scenarios with John, calculations, CNN shapes, LoRA fine-tuning, Pearson traps)
        moderate_pool = [q for q in all_questions if q.get('difficulty') == 'moderate']
        tricky_pool = [q for q in all_questions if q.get('difficulty') == 'tricky']
        random.shuffle(moderate_pool)
        random.shuffle(tricky_pool)
        
        selected = moderate_pool[:30] + tricky_pool[:30]
        random.shuffle(selected)
        
    elif mode == 2:
        # Authentic Real Exam Recall Drill: Exact 60 questions from Master 60Q recall
        recall_pool = [q for q in all_questions if q.get('is_real_recall')]
        random.shuffle(recall_pool)
        selected = recall_pool[:60]
        
    elif mode == 3:
        # Quick Practice Sprint: 15 questions (8 Moderate + 7 Hard/Tricky)
        moderate_pool = [q for q in all_questions if q.get('difficulty') == 'moderate']
        tricky_pool = [q for q in all_questions if q.get('difficulty') == 'tricky']
        random.shuffle(moderate_pool)
        random.shuffle(tricky_pool)
        selected = moderate_pool[:8] + tricky_pool[:7]
        random.shuffle(selected)
        
    num_q = len(selected)
    target_total = 1000 if num_q == 60 else 250
    base_pts = target_total // num_q
    remainder = target_total - (base_pts * num_q)
    
    # Interleave question types Pearson VUE style (Single -> True/False -> Multiple)
    singles = [q for q in selected if q.get('type') == 'Single-Answer Question']
    tfs = [q for q in selected if q.get('type') == 'True or False']
    multis = [q for q in selected if q.get('type') == 'Multiple-Answer Question']
    others = [q for q in selected if q not in singles and q not in tfs and q not in multis]
    
    interleaved = []
    max_len = max(len(singles), len(tfs), len(multis), len(others), 1)
    for i in range(max_len):
        if i < len(singles): interleaved.append(singles[i])
        if i < len(tfs): interleaved.append(tfs[i])
        if i < len(multis): interleaved.append(multis[i])
        if i < len(others): interleaved.append(others[i])
        
    final_questions = interleaved[:num_q]
    
    # Assign point values to match exact target points
    for idx, q in enumerate(final_questions):
        q_copy = dict(q)
        q_copy['exam_pts'] = base_pts + (1 if idx < remainder else 0)
        final_questions[idx] = q_copy
        
    return final_questions

def run_exam_session(questions, mode_title, time_limit_minutes=90):
    total_q = len(questions)
    user_answers = {i: "" for i in range(total_q)}
    flagged = {i: False for i in range(total_q)}
    
    start_time = time.time()
    total_seconds = time_limit_minutes * 60
    
    current_idx = 0
    
    while True:
        elapsed = time.time() - start_time
        remaining = total_seconds - elapsed
        if remaining <= 0:
            cprint("\n⏰ TIME IS UP! The 90-minute examination window has expired.", Colors.RED, bold=True)
            time.sleep(2)
            break
            
        clear_screen()
        q = questions[current_idx]
        
        # Determine Difficulty Tier Label
        diff = q.get('difficulty', 'moderate')
        if diff == 'tricky':
            tier_badge = f"{Colors.MAGENTA}[Level: Hard & Tricky]{Colors.RESET}"
        else:
            tier_badge = f"{Colors.BLUE}[Level: Moderate]{Colors.RESET}"
            
        flag_status = f"{Colors.YELLOW}[★ FLAGGED FOR REVIEW]{Colors.RESET}" if flagged[current_idx] else ""
        
        # Header Bar
        cprint(f"==========================================================================================", Colors.CYAN)
        cprint(f"  HCIA-AI V4.0 EXAM SIMULATOR • {mode_title.upper()}", Colors.BOLD)
        cprint(f"  Question {current_idx + 1} of {total_q}  |  Points: {q['exam_pts']}  |  Time Remaining: {format_time(remaining)}  {flag_status}", Colors.CYAN)
        cprint(f"  Module: {q.get('module', 'General AI')}  |  {tier_badge}  |  Type: {q.get('type', 'Standard')}", Colors.DIM)
        cprint(f"==========================================================================================", Colors.CYAN)
        print()
        
        # Question Text
        cprint(f"Q{current_idx + 1}. {q['question']}", Colors.BOLD)
        print()
        
        # Options
        for opt in q.get('options', []):
            print(f"   {opt}")
        print()
        
        # Current Answer Display
        ans_now = user_answers[current_idx]
        if ans_now:
            cprint(f"Current Selected Answer: {ans_now}", Colors.GREEN, bold=True)
        else:
            cprint("Current Selected Answer: [None - Unanswered]", Colors.DIM)
        print()
        
        # Navigation Instructions
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        cprint("Commands: [A-D] Answer  |  [N]ext  |  [B]ack  |  [F]lag/Unflag  |  [R]eview Grid  |  [Q]uit", Colors.DIM)
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        
        user_input = input(f"{Colors.BOLD}Enter Choice / Command > {Colors.RESET}").strip()
        cmd = user_input.lower()
        
        if not user_input:
            # Enter alone moves to next question
            if current_idx < total_q - 1:
                current_idx += 1
            else:
                chosen_q = show_review_screen(questions, user_answers, flagged, remaining)
                if chosen_q == -1:
                    break
                else:
                    current_idx = chosen_q
            continue
            
        if cmd == 'n':
            if current_idx < total_q - 1:
                current_idx += 1
            else:
                chosen_q = show_review_screen(questions, user_answers, flagged, remaining)
                if chosen_q == -1:
                    break
                else:
                    current_idx = chosen_q
        elif cmd == 'b':
            if current_idx > 0:
                current_idx -= 1
        elif cmd == 'f':
            flagged[current_idx] = not flagged[current_idx]
        elif cmd == 'r':
            chosen_q = show_review_screen(questions, user_answers, flagged, remaining)
            if chosen_q == -1:
                break
            else:
                current_idx = chosen_q
        elif cmd == 'q':
            confirm = input("Are you sure you want to exit the exam early? (y/n): ").strip().lower()
            if confirm == 'y':
                break
        else:
            # Parse answer
            norm = normalize_answer(user_input)
            if norm:
                user_answers[current_idx] = norm
                # Auto-advance to next question if it's Single Choice or True/False
                if q.get('type') in ['Single-Answer Question', 'True or False']:
                    if current_idx < total_q - 1:
                        current_idx += 1
                    else:
                        chosen_q = show_review_screen(questions, user_answers, flagged, remaining)
                        if chosen_q == -1:
                            break
                        else:
                            current_idx = chosen_q
            else:
                cprint("Invalid input! Please enter option letters (e.g. A, B, C, D) or navigation commands.", Colors.RED)
                time.sleep(1)

    # Show Final Diagnostic Report
    generate_score_report(questions, user_answers, mode_title, elapsed=time.time() - start_time)

def show_review_screen(questions, user_answers, flagged, remaining):
    """Pearson VUE Review Screen before final submission"""
    total_q = len(questions)
    while True:
        clear_screen()
        cprint("==========================================================================================", Colors.YELLOW)
        cprint("                        PEARSON VUE EXAM REVIEW SCREEN                                    ", Colors.BOLD)
        cprint(f"  Time Remaining: {format_time(remaining)}  |  Total Items: {total_q}", Colors.YELLOW)
        cprint("==========================================================================================", Colors.YELLOW)
        print()
        
        answered_cnt = sum(1 for a in user_answers.values() if a)
        unanswered_cnt = total_q - answered_cnt
        flagged_cnt = sum(1 for f in flagged.values() if f)
        
        cprint(f"  Status Summary:  [✓] Answered: {answered_cnt}  |  [ ] Unanswered: {unanswered_cnt}  |  [★] Flagged: {flagged_cnt}", Colors.CYAN, bold=True)
        print()
        
        # Display questions in 3 columns
        cols = 3
        rows = (total_q + cols - 1) // cols
        for r in range(rows):
            line_str = ""
            for c in range(cols):
                idx = r + c * rows
                if idx < total_q:
                    ans = user_answers[idx]
                    is_flag = flagged[idx]
                    diff_sym = "[T]" if questions[idx].get('difficulty') == 'tricky' else "[M]"
                    status_symbol = "[✓]" if ans else "[ ]"
                    flag_symbol = "★" if is_flag else " "
                    ans_label = f"({ans})" if ans else "(--)"
                    col_text = f"Q{idx+1:02d} {flag_symbol}{status_symbol}{diff_sym} {ans_label:<5}"
                    line_str += f"{col_text:<28}"
            print(f"  {line_str}")
        print()
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        cprint("Legend: [M] Moderate Level  |  [T] Hard & Tricky Level  |  [✓] Answered  |  [★] Flagged", Colors.DIM)
        cprint("Commands:", Colors.BOLD)
        print("  • Enter question number (1 - 60) to jump directly to that question")
        print("  • Enter 'U' to jump to first unanswered question")
        print("  • Enter 'F' to jump to first flagged question")
        print("  • Enter 'FINISH' to submit your exam and receive final diagnostic score report")
        print("  • Enter 'RETURN' to resume taking the exam")
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        
        choice = input(f"{Colors.BOLD}Review Command > {Colors.RESET}").strip().upper()
        
        if choice in ['FINISH', 'SUBMIT', 'END']:
            if unanswered_cnt > 0:
                cprint(f"\n⚠️ WARNING: You still have {unanswered_cnt} unanswered questions!", Colors.YELLOW, bold=True)
                confirm = input("Are you absolutely sure you want to finish and grade the exam? (yes/no): ").strip().lower()
                if confirm in ['y', 'yes']:
                    return -1
            else:
                return -1
        elif choice in ['RETURN', 'RESUME', 'R', '']:
            return 0
        elif choice == 'U':
            for i in range(total_q):
                if not user_answers[i]:
                    return i
            cprint("No unanswered questions remaining!", Colors.GREEN)
            time.sleep(1)
        elif choice == 'F':
            for i in range(total_q):
                if flagged[i]:
                    return i
            cprint("No flagged questions remaining!", Colors.GREEN)
            time.sleep(1)
        elif choice.isdigit():
            q_num = int(choice)
            if 1 <= q_num <= total_q:
                return q_num - 1
            else:
                cprint(f"Please enter a valid question number between 1 and {total_q}!", Colors.RED)
                time.sleep(1)
        else:
            cprint("Invalid command. Please try again.", Colors.RED)
            time.sleep(1)

def generate_score_report(questions, user_answers, mode_title, elapsed):
    clear_screen()
    total_q = len(questions)
    earned_pts = 0
    max_pts = sum(q['exam_pts'] for q in questions)
    
    correct_count = 0
    incorrect_list = []
    
    # Tracking stats
    module_stats = {}
    type_stats = {}
    difficulty_stats = {
        'moderate': {'earned': 0, 'total': 0, 'correct': 0, 'count': 0},
        'tricky': {'earned': 0, 'total': 0, 'correct': 0, 'count': 0}
    }
    
    for idx, q in enumerate(questions):
        user_ans = user_answers[idx]
        correct_ans = normalize_answer(q.get('answer', ''))
        is_correct = (user_ans == correct_ans)
        
        pts = q['exam_pts']
        mod = q.get('module', 'General')
        qtype = q.get('type', 'Standard')
        diff = q.get('difficulty', 'moderate')
        
        # Difficulty breakdown
        difficulty_stats[diff]['total'] += pts
        difficulty_stats[diff]['count'] += 1
        
        # Module breakdown
        if mod not in module_stats:
            module_stats[mod] = {'earned': 0, 'total': 0, 'correct': 0, 'count': 0}
        module_stats[mod]['total'] += pts
        module_stats[mod]['count'] += 1
        
        # Type breakdown
        if qtype not in type_stats:
            type_stats[qtype] = {'correct': 0, 'count': 0}
        type_stats[qtype]['count'] += 1
        
        if is_correct:
            earned_pts += pts
            correct_count += 1
            difficulty_stats[diff]['earned'] += pts
            difficulty_stats[diff]['correct'] += 1
            module_stats[mod]['earned'] += pts
            module_stats[mod]['correct'] += 1
            type_stats[qtype]['correct'] += 1
        else:
            incorrect_list.append({
                'num': idx + 1,
                'question': q['question'],
                'options': q.get('options', []),
                'user_ans': user_ans if user_ans else 'Unanswered',
                'correct_ans': correct_ans,
                'explanation': q.get('explanation', ''),
                'module': mod,
                'difficulty': diff,
                'points': pts
            })
            
    pct = (earned_pts / max_pts) * 100 if max_pts > 0 else 0
    is_passed = (earned_pts >= 600) if max_pts == 1000 else (pct >= 60.0)
    
    # Render Report
    cprint("==========================================================================================", Colors.BLUE)
    cprint("                   HUAWEI HCIA-AI V4.0 • OFFICIAL EXAM SCORE REPORT                       ", Colors.BOLD)
    cprint("==========================================================================================", Colors.BLUE)
    print()
    print(f"  Candidate Name:    Umed Jamal Nouri")
    print(f"  Examination Mode:  {mode_title}")
    print(f"  Date & Time:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Time Elapsed:      {format_time(elapsed)}")
    print(f"  Total Questions:   {total_q} (Combines Moderate & Hard/Tricky Questions)")
    print(f"  Passing Score:     600 / 1000 Points (60.0%)")
    print()
    cprint("------------------------------------------------------------------------------------------", Colors.DIM)
    
    # Score Banner
    if is_passed:
        cprint(f"  FINAL SCORE: {earned_pts} / {max_pts} Points  ({pct:.1f}%)", Colors.GREEN, bold=True)
        cprint("  VERDICT:     CONGRATULATIONS! YOU PASSED", Colors.GREEN, bold=True)
    else:
        cprint(f"  FINAL SCORE: {earned_pts} / {max_pts} Points  ({pct:.1f}%)", Colors.RED, bold=True)
        cprint("  VERDICT:     DID NOT PASS - RETAKE RECOMMENDED", Colors.RED, bold=True)
        pts_needed = 600 - earned_pts
        cprint(f"  Gap to Pass: You need {pts_needed} more points to reach the 600-point threshold.", Colors.YELLOW)
        
    cprint("------------------------------------------------------------------------------------------", Colors.DIM)
    print()
    
    # Difficulty Tier Breakdown
    cprint("Performance by Difficulty Level:", Colors.BOLD)
    mod_stat = difficulty_stats['moderate']
    tri_stat = difficulty_stats['tricky']
    mod_pct = (mod_stat['correct'] / mod_stat['count']) * 100 if mod_stat['count'] > 0 else 0
    tri_pct = (tri_stat['correct'] / tri_stat['count']) * 100 if tri_stat['count'] > 0 else 0
    
    print(f"  • Moderate Level   : {mod_stat['correct']:>2}/{mod_stat['count']:<2} correct ({mod_pct:>5.1f}%) | {mod_stat['earned']}/{mod_stat['total']} pts")
    print(f"  • Hard & Tricky Level  : {tri_stat['correct']:>2}/{tri_stat['count']:<2} correct ({tri_pct:>5.1f}%) | {tri_stat['earned']}/{tri_stat['total']} pts")
    print()
    
    # Question Type Performance
    cprint("Performance by Question Type:", Colors.BOLD)
    for qtype, s in type_stats.items():
        type_pct = (s['correct'] / s['count']) * 100 if s['count'] > 0 else 0
        print(f"  • {qtype:<28} : {s['correct']}/{s['count']} correct ({type_pct:.1f}%)")
    print()
    
    # Module Breakdown
    cprint("Performance by Curriculum Module:", Colors.BOLD)
    for mod, s in module_stats.items():
        m_pct = (s['earned'] / s['total']) * 100 if s['total'] > 0 else 0
        bar = "█" * int(m_pct // 10) + "░" * (10 - int(m_pct // 10))
        color = Colors.GREEN if m_pct >= 60 else Colors.RED
        cprint(f"  • {mod:<45} [{bar}] {s['earned']:>3}/{s['total']:<3} pts ({m_pct:>5.1f}%)", color)
    print()
    
    # Post-Exam Options
    while True:
        cprint("==========================================================================================", Colors.BLUE)
        print("Options:")
        print("  [1] Review Incorrect Questions with Detailed Explanations & Slide Citations")
        print("  [2] Save Diagnostic Score Report to Text File")
        print("  [3] Retake New Exam (Fresh Shuffled Questions)")
        print("  [Q] Exit Simulator")
        cprint("==========================================================================================", Colors.BLUE)
        
        rep_choice = input(f"{Colors.BOLD}Select Option > {Colors.RESET}").strip().lower()
        if rep_choice == '1':
            review_missed_questions(incorrect_list)
        elif rep_choice == '2':
            save_report_file(questions, user_answers, earned_pts, max_pts, pct, is_passed, module_stats, type_stats, difficulty_stats, incorrect_list, mode_title)
        elif rep_choice == '3':
            main()
            return
        elif rep_choice in ['q', 'exit', 'quit']:
            cprint("\nThank you for using the HCIA-AI V4.0 Exam Simulator. Best of luck on your retake!", Colors.CYAN, bold=True)
            break
        else:
            cprint("Invalid choice, please select 1, 2, 3, or Q.", Colors.RED)

def review_missed_questions(incorrect_list):
    if not incorrect_list:
        cprint("\n🎉 PERFECT SCORE! You did not miss any questions in this examination session!", Colors.GREEN, bold=True)
        input("\nPress [Enter] to return...")
        return
        
    clear_screen()
    cprint("==========================================================================================", Colors.RED)
    cprint(f"               DETAILED REVIEW OF MISSED QUESTIONS ({len(incorrect_list)} ITEMS)                   ", Colors.BOLD)
    cprint("==========================================================================================", Colors.RED)
    print()
    
    for item in incorrect_list:
        tier_str = "Hard & Tricky" if item.get('difficulty') == 'tricky' else "Moderate"
        cprint(f"Question #{item['num']} • {item['module']} • [{tier_str}] ({item['points']} Points)", Colors.YELLOW, bold=True)
        print(f"Prompt: {item['question']}")
        print()
        print("Options:")
        for opt in item['options']:
            print(f"  {opt}")
        print()
        cprint(f"Your Answer:     {item['user_ans']}", Colors.RED, bold=True)
        cprint(f"Correct Answer:  {item['correct_ans']}", Colors.GREEN, bold=True)
        if item['explanation']:
            print()
            cprint("Official Huawei Technical Explanation & Slide Citation:", Colors.CYAN, bold=True)
            clean_expl = item['explanation'].replace('<b>', '').replace('</b>', '').replace('<i>', '').replace('</i>', '').replace('<br/>', '\n')
            print(f"  {clean_expl}")
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        print()
        
    input("\nPress [Enter] to return to Score Report...")

def save_report_file(questions, user_answers, earned_pts, max_pts, pct, is_passed, module_stats, type_stats, difficulty_stats, incorrect_list, mode_title):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"HCIA_AI_Exam_Report_{timestamp}.txt"
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("==========================================================================================\n")
        f.write("                   HUAWEI HCIA-AI V4.0 • OFFICIAL EXAM SCORE REPORT                       \n")
        f.write("==========================================================================================\n\n")
        f.write(f"Candidate Name:    Umed Jamal Nouri\n")
        f.write(f"Examination Mode:  {mode_title}\n")
        f.write(f"Date & Time:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Score:             {earned_pts} / {max_pts} Points ({pct:.1f}%)\n")
        f.write(f"Verdict:           {'PASS' if is_passed else 'FAIL'}\n\n")
        
        f.write("Performance by Difficulty Level:\n")
        mod_stat = difficulty_stats['moderate']
        tri_stat = difficulty_stats['tricky']
        mod_pct = (mod_stat['correct'] / mod_stat['count']) * 100 if mod_stat['count'] > 0 else 0
        tri_pct = (tri_stat['correct'] / tri_stat['count']) * 100 if tri_stat['count'] > 0 else 0
        f.write(f"  • Moderate Level  : {mod_stat['correct']}/{mod_stat['count']} correct ({mod_pct:.1f}%) | {mod_stat['earned']}/{mod_stat['total']} pts\n")
        f.write(f"  • Hard & Tricky Level : {tri_stat['correct']}/{tri_stat['count']} correct ({tri_pct:.1f}%) | {tri_stat['earned']}/{tri_stat['total']} pts\n\n")
        
        f.write("Performance by Curriculum Module:\n")
        for mod, s in module_stats.items():
            m_pct = (s['earned'] / s['total']) * 100 if s['total'] > 0 else 0
            f.write(f"  • {mod:<45} : {s['earned']:>3}/{s['total']:<3} pts ({m_pct:>5.1f}%)\n")
        f.write("\n")
        
        if incorrect_list:
            f.write("==========================================================================================\n")
            f.write(f"Missed Questions ({len(incorrect_list)} Items):\n")
            f.write("==========================================================================================\n\n")
            for item in incorrect_list:
                f.write(f"Q#{item['num']}: {item['question']}\n")
                f.write(f"Your Answer:    {item['user_ans']}\n")
                f.write(f"Correct Answer: {item['correct_ans']}\n")
                if item['explanation']:
                    clean_expl = item['explanation'].replace('<b>', '').replace('</b>', '').replace('<i>', '').replace('</i>', '').replace('<br/>', '\n')
                    f.write(f"Explanation:    {clean_expl}\n")
                f.write("------------------------------------------------------------------------------------------\n\n")
                
    cprint(f"\n[OK] Diagnostic score report saved successfully to: {filepath}", Colors.GREEN, bold=True)
    time.sleep(2)

def main():
    db = load_database()
    all_qs = db.get('questions', [])
    
    while True:
        clear_screen()
        cprint("==========================================================================================", Colors.CYAN)
        cprint("🎓  HUAWEI CERTIFIED ICT ASSOCIATE (HCIA-AI V4.0) • EXAM SIMULATOR", Colors.BOLD)
        cprint("    Simulating Authentic Pearson VUE Computer-Based Testing Environment", Colors.CYAN)
        cprint("    Curated by: Umed Jamal Nouri  •  Release v1.3.0  •  github.com/UmedJaMala", Colors.DIM)
        cprint("==========================================================================================", Colors.CYAN)
        print()
        cprint("Select Examination Mode:", Colors.BOLD)
        print()
        print("  [1] Official Real Exam Simulation (Combines Moderate & Hard/Tricky in ONE Exam)")
        print("      • 60 randomized questions combining BOTH Moderate & Hard/Tricky questions in ONE exam:")
        print("        - 30 Moderate questions (core concepts, definitions, foundational ML/DL)")
        print("        - 30 Hard & Tricky questions (John scenarios, calculations, CNN shapes, LoRA fine-tuning)")
        print("      • Exact 1000 points scoring • 90-minute live countdown timer")
        print()
        print("  [2] Real Exam Recall Drill (Authentic Pearson VUE Exam Recalls)")
        print("      • Authentic 60 questions directly recalled from recent Pearson VUE test-takers")
        print("      • Step-by-step derivations and official slide citations included")
        print()
        print("  [3] Quick Practice Sprint (15 Mixed Questions)")
        print("      • 15 mixed questions (Moderate + Tricky) for rapid 20-minute daily review sessions")
        print()
        print("  [Q] Exit Simulator")
        print()
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        
        choice = input(f"{Colors.BOLD}Enter Mode (1, 2, 3, or Q) > {Colors.RESET}").strip().lower()
        
        if choice == '1':
            selected_qs = select_exam_questions(all_qs, mode=1)
            run_exam_session(selected_qs, "Unified Comprehensive Exam (Moderate + Hard/Tricky Combined)")
            break
        elif choice == '2':
            selected_qs = select_exam_questions(all_qs, mode=2)
            run_exam_session(selected_qs, "Real Exam Recall Drill (60 Questions)")
            break
        elif choice == '3':
            selected_qs = select_exam_questions(all_qs, mode=3)
            run_exam_session(selected_qs, "Quick Practice Sprint (15 Questions)", time_limit_minutes=20)
            break
        elif choice in ['q', 'exit', 'quit']:
            cprint("\nExiting Exam Simulator. Goodbye!", Colors.CYAN)
            break
        else:
            cprint("Invalid choice, please select 1, 2, 3, or Q.", Colors.RED)
            time.sleep(1)

if __name__ == '__main__':
    main()
