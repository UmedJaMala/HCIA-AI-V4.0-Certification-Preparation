#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Root Launcher for Huawei HCIA-AI V4.0 Interactive Exam Simulator.
Redirects execution to 03_Interactive_Exam_Simulator/take_exam.py.
"""
import sys
import os

target = os.path.join(os.path.dirname(os.path.abspath(__file__)), '03_Interactive_Exam_Simulator', 'take_exam.py')
if os.path.exists(target):
    with open(target, 'r', encoding='utf-8') as f:
        code = f.read()
    exec(compile(code, target, 'exec'), {'__name__': '__main__', '__file__': target})
else:
    print(f"Error: Simulator script not found at {target}")
    sys.exit(1)
