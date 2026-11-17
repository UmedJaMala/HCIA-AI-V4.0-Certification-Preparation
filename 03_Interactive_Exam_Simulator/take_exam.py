#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🎓 HUAWEI HCIA-AI V4.0 (H13-311_V4.0) • OFFICIAL INTERACTIVE EXAM SIMULATOR
Authentic Pearson VUE Testing Environment • 60 Questions • 1000 Points • 90 Minutes
Single Source of Truth: 01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf
Audited & Verified Release v2.0.0
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

# Resolve Database Path robustly
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
POSSIBLE_PATHS = [
    os.path.join(CURRENT_DIR, 'exam_database.json'),
    os.path.join(CURRENT_DIR, '03_Interactive_Exam_Simulator', 'exam_database.json'),
    os.path.join(os.path.dirname(CURRENT_DIR), '03_Interactive_Exam_Simulator', 'exam_database.json'),
]

DB_PATH = None
for p in POSSIBLE_PATHS:
    if os.path.exists(p):
        DB_PATH = p
        break

def load_database():
    if not DB_PATH or not os.path.exists(DB_PATH):
        cprint(f"Error: Question database not found! Checked locations:\n" + "\n".join(POSSIBLE_PATHS), Colors.RED, bold=True)
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
    1: Comprehensive Pearson VUE Real Exam (Verified Recalls + Moderate/Tricky - 60Q)
    2: Verified Official & Recalled Questions Only (100% verified against official slides - 60Q)
    3: Quick Practice Sprint (Verified Items Only - 15Q)
    4: Full Question Bank Practice (Includes AI supplementary practice items - 60Q)
    """
    selected = []
    
    if mode == 1:
        # High-accuracy official simulation: Prioritizes verified recalls + verified curriculum items
        recall_pool = [q for q in all_questions if q.get('is_real_recall')]
        random.shuffle(recall_pool)
        selected = recall_pool[:60]
        
    elif mode == 2:
        # STRICT VERIFIED FILTER MODE: Strictly 100% verified against official slides
        verified_pool = [q for q in all_questions if q.get('verified_against_official_slides') is True]
        random.shuffle(verified_pool)
        selected = verified_pool[:60]
        
    elif mode == 3:
        # Quick Practice Sprint: 15 questions from verified pool for quick drill
        verified_pool = [q for q in all_questions if q.get('verified_against_official_slides') is True]
        random.shuffle(verified_pool)
        selected = verified_pool[:15]
        
    elif mode == 4:
        # Full Bank Practice: Mixed pool excluding legacy outdated V3.0 items
        active_pool = [q for q in all_questions if q.get('audit_status') != 'LEGACY_V3_OUTDATED']
        random.shuffle(active_pool)
        selected = active_pool[:60]
        
    num_q = len(selected)
    target_total = 1000 if num_q == 60 else 250
    base_pts = target_total // num_q if num_q > 0 else 0
    remainder = target_total - (base_pts * num_q) if num_q > 0 else 0
    
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
    show_slide_ref = {i: False for i in range(total_q)}
    
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
        
        # Determine Verification Badge
        is_verified = q.get('verified_against_official_slides', False)
        audit_stat = q.get('audit_status', '')
        if is_verified:
            ver_badge = f"{Colors.GREEN}[✓ VERIFIED OFFICIAL SLIDE CITATION]{Colors.RESET}"
        elif audit_stat == 'LEGACY_V3_OUTDATED':
            ver_badge = f"{Colors.RED}[⚠️ LEGACY V3.0 OUTDATED]{Colors.RESET}"
        else:
            ver_badge = f"{Colors.YELLOW}[AI SUPPLEMENTARY]{Colors.RESET}"
            
        diff = q.get('difficulty', 'moderate')
        tier_badge = f"{Colors.MAGENTA}[Level: Hard & Tricky]{Colors.RESET}" if diff == 'tricky' else f"{Colors.BLUE}[Level: Moderate]{Colors.RESET}"
        flag_status = f"{Colors.YELLOW}[★ FLAGGED FOR REVIEW]{Colors.RESET}" if flagged[current_idx] else ""
        
        # Header Bar
        cprint("==========================================================================================", Colors.CYAN)
        cprint(f"  HCIA-AI V4.0 EXAM SIMULATOR • {mode_title.upper()}", Colors.BOLD)
        cprint(f"  Question {current_idx + 1} of {total_q}  |  Points: {q['exam_pts']}  |  Time Remaining: {format_time(remaining)}  {flag_status}", Colors.CYAN)
        cprint(f"  Module: {q.get('module', 'General AI')}  |  {tier_badge}  |  {ver_badge}", Colors.DIM)
        cprint("==========================================================================================", Colors.CYAN)
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
        
        # Inline Official Slide Reference Toggle Box [S]
        if show_slide_ref[current_idx]:
            cprint("┌────────────────────────────────────────────────────────────────────────────────────────┐", Colors.YELLOW)
            cprint("│ 📖 OFFICIAL HUAWEI SOURCE REFERENCE (Single Source of Truth)                            │", Colors.YELLOW, bold=True)
            cprint("├────────────────────────────────────────────────────────────────────────────────────────┤", Colors.YELLOW)
            ref_text = q.get('official_source_reference', 'No reference available.')
            # Wrap reference lines
            for chunk in ref_text.split(' | '):
                cprint(f"│ • {chunk}", Colors.CYAN)
            cprint("│ File: 01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf               │", Colors.DIM)
            cprint("└────────────────────────────────────────────────────────────────────────────────────────┘", Colors.YELLOW)
            print()
            
        # Navigation Instructions
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        cprint("Commands: [A-D] Answer  |  [S] Toggle Slide Ref  |  [N]ext  |  [B]ack  |  [F]lag  |  [R]eview  |  [Q]uit", Colors.DIM)
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        
        user_input = input(f"{Colors.BOLD}Enter Choice / Command > {Colors.RESET}").strip()
        cmd = user_input.lower()
        
        if not user_input:
            if current_idx < total_q - 1:
                current_idx += 1
            else:
                chosen_q = show_review_screen(questions, user_answers, flagged, remaining)
                if chosen_q == -1:
                    break
                else:
                    current_idx = chosen_q
            continue
            
        if cmd == 's':
            show_slide_ref[current_idx] = not show_slide_ref[current_idx]
            continue
        elif cmd == 'n':
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
                cprint("Invalid input! Enter option letters [A-D], [S] to toggle slide citation, or navigation commands.", Colors.RED)
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
                    ver_sym = "★" if questions[idx].get('verified_against_official_slides') else "·"
                    status_symbol = "[✓]" if ans else "[ ]"
                    flag_symbol = "F" if is_flag else " "
                    ans_label = f"({ans})" if ans else "(--)"
                    col_text = f"Q{idx+1:02d} {ver_sym}{flag_symbol}{status_symbol}{diff_sym} {ans_label:<5}"
                    line_str += f"{col_text:<28}"
            print(f"  {line_str}")
        print()
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        cprint("Legend: ★ Verified Slide Citation  |  [M] Moderate  |  [T] Tricky  |  [✓] Answered  |  F Flagged", Colors.DIM)
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
        
        difficulty_stats[diff]['total'] += pts
        difficulty_stats[diff]['count'] += 1
        
        if mod not in module_stats:
            module_stats[mod] = {'earned': 0, 'total': 0, 'correct': 0, 'count': 0}
        module_stats[mod]['total'] += pts
        module_stats[mod]['count'] += 1
        
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
                'official_ref': q.get('official_source_reference', ''),
                'module': mod,
                'difficulty': diff,
                'points': pts,
                'is_verified': q.get('verified_against_official_slides', False)
            })
            
    pct = (earned_pts / max_pts) * 100 if max_pts > 0 else 0
    is_passed = (earned_pts >= 600) if max_pts == 1000 else (pct >= 60.0)
    
    # Render Report
    cprint("==========================================================================================", Colors.BLUE)
    cprint("                   HUAWEI HCIA-AI V4.0 • OFFICIAL EXAM SCORE REPORT                       ", Colors.BOLD)
    cprint("==========================================================================================", Colors.BLUE)
    print()
    print(f"  Candidate:         HCIA-AI V4.0 Certification Candidate")
    print(f"  Examination Mode:  {mode_title}")
    print(f"  Date & Time:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Time Elapsed:      {format_time(elapsed)}")
    print(f"  Total Questions:   {total_q}")
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
    
    # Module Breakdown with pass/fail threshold
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
        print("  [1] Review Missed Questions (With Verbatim Official Slide References & Traps)")
        print("  [2] Save Diagnostic Score Report to Text File")
        print("  [3] Retake New Exam")
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
            cprint("\nGood luck on your official HCIA-AI V4.0 Pearson VUE retake!", Colors.CYAN, bold=True)
            break
        else:
            cprint("Invalid choice, please select 1, 2, 3, or Q.", Colors.RED)

def review_missed_questions(incorrect_list):
    if not incorrect_list:
        cprint("\n🎉 PERFECT SCORE! You answered every question correctly in this session!", Colors.GREEN, bold=True)
        input("\nPress [Enter] to return...")
        return
        
    clear_screen()
    cprint("==========================================================================================", Colors.RED)
    cprint(f"               DETAILED REVIEW OF MISSED QUESTIONS ({len(incorrect_list)} ITEMS)                   ", Colors.BOLD)
    cprint("==========================================================================================", Colors.RED)
    print()
    
    for item in incorrect_list:
        tier_str = "Hard & Tricky" if item.get('difficulty') == 'tricky' else "Moderate"
        ver_tag = "[✓ VERIFIED OFFICIAL CITATION]" if item['is_verified'] else "[AI SUPPLEMENTARY]"
        cprint(f"Question #{item['num']} • {item['module']} • [{tier_str}] • {ver_tag} ({item['points']} Points)", Colors.YELLOW, bold=True)
        print(f"Prompt: {item['question']}")
        print()
        print("Options:")
        for opt in item['options']:
            print(f"  {opt}")
        print()
        cprint(f"Your Answer:     {item['user_ans']}", Colors.RED, bold=True)
        cprint(f"Correct Answer:  {item['correct_ans']}", Colors.GREEN, bold=True)
        print()
        
        # Display Official Slide Reference
        if item.get('official_ref'):
            cprint("┌────────────────────────────────────────────────────────────────────────────────────────┐", Colors.CYAN)
            cprint("│ 📖 OFFICIAL HUAWEI SLIDE REFERENCE (Source of Truth)                                    │", Colors.CYAN, bold=True)
            cprint("├────────────────────────────────────────────────────────────────────────────────────────┤", Colors.CYAN)
            for chunk in item['official_ref'].split(' | '):
                cprint(f"│ {chunk}", Colors.YELLOW)
            cprint("│ Source File: 01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf        │", Colors.DIM)
            cprint("└────────────────────────────────────────────────────────────────────────────────────────┘", Colors.CYAN)
            
        if item.get('explanation'):
            clean_expl = item['explanation'].replace('<b>', '').replace('</b>', '').replace('<i>', '').replace('</i>', '').replace('<br/>', '\n')
            print(f"\nTechnical Explanation & Trap Analysis:\n{clean_expl}")
            
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        print()
        
    input("\nPress [Enter] to return to Score Report...")

def save_report_file(questions, user_answers, earned_pts, max_pts, pct, is_passed, module_stats, type_stats, difficulty_stats, incorrect_list, mode_title):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"HCIA_AI_Exam_Report_{timestamp}.txt"
    filepath = os.path.join(CURRENT_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("==========================================================================================\n")
        f.write("                   HUAWEI HCIA-AI V4.0 • OFFICIAL EXAM SCORE REPORT                       \n")
        f.write("==========================================================================================\n\n")
        f.write(f"Examination Mode:  {mode_title}\n")
        f.write(f"Date & Time:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Score:             {earned_pts} / {max_pts} Points ({pct:.1f}%)\n")
        f.write(f"Verdict:           {'PASS' if is_passed else 'FAIL'}\n\n")
        
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
                if item.get('official_ref'):
                    f.write(f"Official Slide Reference: {item['official_ref']}\n")
                if item.get('explanation'):
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
        cprint("    Authentic Pearson VUE Computer-Based Testing Environment • Audited v2.0", Colors.CYAN)
        cprint("    Single Source of Truth: 01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf", Colors.DIM)
        cprint("==========================================================================================", Colors.CYAN)
        print()
        cprint("Select Examination Mode:", Colors.BOLD)
        print()
        cprint("  [1] Official Real Exam Simulation (Authentic 60-Question Pearson VUE Exam)", Colors.GREEN, bold=True)
        print("      • 60 authentic recalled questions matching Pearson VUE distribution")
        print("      • 1000 points scoring • 90-minute live countdown timer")
        print()
        cprint("  [2] [Verified Official & Recalled Questions Only] ⭐ RECOMMENDED FOR RETAKE", Colors.YELLOW, bold=True)
        print("      • Strictly restricted to questions verified against official 473 slides")
        print("      • Press [S] during exam to view verbatim slide proof & trap notes inline")
        print("      • 100% elimination of AI filler and outdated V3.0 questions")
        print()
        print("  [3] Quick Practice Sprint (15 Verified Questions)")
        print("      • Rapid 20-minute daily review session using verified official recall items")
        print()
        print("  [4] Full Question Bank Practice (Includes Supplementary AI Review Items)")
        print("      • Practice on wider pool (excludes obsolete V3.0 DaVinci/CANN/MindSpore questions)")
        print()
        print("  [Q] Exit Simulator")
        print()
        cprint("------------------------------------------------------------------------------------------", Colors.DIM)
        
        choice = input(f"{Colors.BOLD}Enter Mode (1, 2, 3, 4, or Q) > {Colors.RESET}").strip().lower()
        
        if choice == '1':
            selected_qs = select_exam_questions(all_qs, mode=1)
            run_exam_session(selected_qs, "Official Real Exam Simulation (60 Questions)")
            break
        elif choice == '2':
            selected_qs = select_exam_questions(all_qs, mode=2)
            run_exam_session(selected_qs, "Verified Official & Recalled Questions Only (60 Questions)")
            break
        elif choice == '3':
            selected_qs = select_exam_questions(all_qs, mode=3)
            run_exam_session(selected_qs, "Quick Practice Sprint (15 Questions)", time_limit_minutes=20)
            break
        elif choice == '4':
            selected_qs = select_exam_questions(all_qs, mode=4)
            run_exam_session(selected_qs, "Full Bank Practice (60 Questions)")
            break
        elif choice in ['q', 'exit', 'quit']:
            cprint("\nExiting Exam Simulator. Good luck with your study!", Colors.CYAN)
            break
        else:
            cprint("Invalid choice, please select 1, 2, 3, 4, or Q.", Colors.RED)
            time.sleep(1)

if __name__ == '__main__':
    main()
