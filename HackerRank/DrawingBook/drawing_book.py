# Problem: https://www.hackerrank.com/challenges/drawing-book/problem
# A teacher asks the class to open their books to a page number. A student can either start turning pages from the
# front of the book or from the back of the book. They always turn pages one at a time. When they open the book,
# page 1 is always on the right side. When they flip page 1, they see pages 2 and 3. Each page except the last page will
# always be printed on both sides. The last page may only be printed on the front, given the length of the book.
# If the book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn?
# They can start at the beginning or the end of the book. Given n and p, find and print the minimum number of pages that
# must be turned in order to arrive at page p.
# Example: n = 5, p = 3
# Using the diagram above, if the student wants to get to page 3, they open the book to page 1, flip 1 page and they are
# on the correct page. If they open the book to the last page, page 5, they turn 1 page and are at the correct page. Return 1.


def page_count(n, p):
    white_pages = 2 if n % 2 == 0 else 1
    pages = list(range(n + white_pages))
    pages_to_turn_ltr = pages.index(p) // 2
    pages.reverse()
    pages_to_turn_rtl = pages.index(p) // 2

    return min(pages_to_turn_ltr, pages_to_turn_rtl)
