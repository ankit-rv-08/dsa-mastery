# dsa-mastery
“Structured DSA learning and practice with detailed notes”

## Arrays Module

### Hour 1: Linear Search
[hour1_linear_search.py](arrays/hour1_linear_search.py)
- Implements linear search to find a target in a list
- User input, iteration, index reporting
- Time complexity: O(n)
---

### Hour 2: Find Minimum and Maximum
[hour2_find_min_max.py](arrays/hour2_find_min_max.py)
- Finds the smallest and largest values in a user-entered list
- Handles empty input gracefully
- Reinforces array traversal and comparison logic

---

### Hour 3: Binary Search and Basic Sorting Algorithms

- Implemented Linear Search in Hour 1, Min/Max in Hour 2.
- This hour includes: Bubble Sort, Selection Sort, and Merge Sort implementations.
- Introduced sorting techniques and explained time and space complexity.

**Scripts:**
- [hour3_bubble_sort.py](hour3_bubble_sort.py)
- [hour3_selection_sort.py](hour3_selection_sort.py)
- [hour3_merge_sort.py](arrays/hour3_merge_sort.py)

## Hour 4 – Two Sum Problem & Sliding Window

- Implemented brute force and hash map (dictionary) solutions for the Two Sum problem.
- Introduced sliding window technique for contiguous subarray processing.
- Essential prep for interviews and algorithmic challenges.

**Scripts:**
- [hour4_two_sum.py](arrays/hour4_two_sum.py)
- [hour4_max_sum_subarray.py](arrays/hour4_max_sum_subarray.py)


---

## 📊 Current Progress (Updated Oct 27, 2025)

**Total Problems Solved:** 8/350 (2.3%)  
**Hours Invested:** 3  
**Patterns Mastered:** 5  
**Current Streak:** 🔥 2 days  

| Category | Solved | Target | Progress |
|----------|--------|--------|----------|
| Arrays | 2 | 40 | ███░░░░░░░ 5% |
| Strings | 3 | 30 | ████░░░░░░ 10% |
| Sliding Window | 3 | 20 | ██████░░░░ 15% |
| Two Pointers | 2 | 20 | ████░░░░░░ 10% |
| HashMap/Set | 5 | 25 | ████████░░ 20% |

---

## 📝 Problems Solved (Oct 26-27, 2025)

### Arrays & Two Pointers
| # | Problem | Difficulty | Pattern | Date | Status |
|---|---------|-----------|---------|------|--------|
| 1 | Two Sum | Easy | HashMap | Oct 26 | ✅ |
| 125 | Valid Palindrome | Easy | Two Pointers | Oct 26 | ✅ |

### Strings & HashMaps
| # | Problem | Difficulty | Pattern | Date | Status |
|---|---------|-----------|---------|------|--------|
| 242 | Valid Anagram | Easy | HashMap Frequency | Oct 26 | ✅ |
| 217 | Contains Duplicate | Easy | Set | Oct 26 | ✅ |
| 49 | Group Anagrams | Medium | Sorted Key | Oct 26 | ✅ |

### Sliding Window
| # | Problem | Difficulty | Pattern | Date | Status |
|---|---------|-----------|---------|------|--------|
| 485 | Max Consecutive Ones | Easy | Sliding Window | Oct 27 | ✅ |
| 121 | Best Time to Buy/Sell Stock | Easy | Sliding Window | Oct 27 | ✅ |
| 3 | Longest Substring Without Repeating | Medium | Sliding Window + Set | Oct 27 | ✅ |

---

## 🔥 Patterns Mastered

✅ **HashMap** - O(n) frequency counting, complement search  
✅ **Two Pointers** - Opposite ends, moving toward center  
✅ **Set** - O(1) duplicate detection, uniqueness checks  
✅ **Sorted Keys** - Anagram grouping, normalization  
✅ **Sliding Window** - Dynamic subarray/substring optimization  

---

## 💡 Key Takeaways (Week 1)

### HashMap Pattern
- Store `{value: index}` for O(1) complement lookup
- Frequency counting: `count[char] = count.get(char, 0) + 1`
- Converts O(n²) brute force to O(n)

### Sliding Window Pattern
- Maintain valid window with two pointers (left, right)
- Expand right to grow window, shrink left when invalid
- Track maximum valid window size
- Converts O(n²) subarray checks to O(n)

### Set for Duplicates
- `len(set(arr)) != len(arr)` instantly detects duplicates
- O(1) membership checking
- Perfect for "seen before" checks

---

## 🎯 Current Focus

**Week 1 Goal:** Master foundational patterns (Arrays, Strings, Sliding Window)  
**Week 2 Goal:** Mixed pattern practice, increase speed  
**Month 1 Goal:** 60+ problems, all easy/medium patterns solid  

**Daily Target:** 2-3 problems (6 hours of focused work)  
**Mentored by:** Sarge Ghost 🎖️  
**Target Role:** 15-20 LPA Cloud/AI/DevOps Engineer by Dec 2026  

---



