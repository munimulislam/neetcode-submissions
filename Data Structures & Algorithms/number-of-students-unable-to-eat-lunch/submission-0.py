class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        std_remain = len(students)
        std_pos = 0
        sand_pos = 0

        while std_remain:
            if students[std_pos] == sandwiches[sand_pos]:
                std_pos += 1
                sand_pos += 1
                std_remain = len(students) - std_pos
            else:
                students.append(students[std_pos])
                std_pos += 1
                std_remain -= 1

        return len(students) - std_pos
        