-- 学生ごとの受講講座を表示

SELECT s.student_name, c.course_name -- 生徒名とコース名 
FROM student_courses sc -- course_id と student_id を持つ中間テーブル
JOIN students s ON sc.student_id = s.student_id
JOIN courses c ON sc.course_id = c.course_id;

/* students テーブルは、student_courses テーブルの
   student_id と students テーブルの student_id と同じ */
/* courses テーブルは、student_courses テーブルの
   couse_id と courses テーブルの course_id と同じ */

/*
    students               student_courses           courses
    ┌──────────────┐       ┌────────────────┐        ┌────────────────────────┐
    │ student_id   │◄────► │ student_id     │        │                        │
    │ student_name │       │ course_id      │◄──────►│ course_id              │
    └──────────────┘       └────────────────┘        │ course_name            │
                                                     └────────────────────────┘ */