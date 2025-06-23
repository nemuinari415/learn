-- 各講座に割り当てられている講師の名前を表示
SELECT c.course_name, t.teacher_name 
  FROM teachers t
  JOIN courses c ON c.teacher_id = t.teacher_id