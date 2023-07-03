cmake_minimum_required (VERSION 3.8)

project ("EulerProblems")

set(SRC_FOLDER1 "P1-50/")

add_executable(P4 "${SRC_FOLDER1}P4_largest_palindrome.cpp")
add_executable(P5 "${SRC_FOLDER1}P5_smallest_multiple.cpp")
add_executable(P6 "${SRC_FOLDER1}P6_sum_square_difference.cpp")
add_executable(P7 "${SRC_FOLDER1}P7_10001st_prime.cpp")
add_executable(P8 "${SRC_FOLDER1}P8_largest_product_in_a_series")
add_executable(P9 "${SRC_FOLDER1}P9_special_pythagorean_triplet.cpp")

add_executable(P10 "${SRC_FOLDER1}P10_summation_of_primes.cpp")
add_executable(P11 "${SRC_FOLDER1}P11_largest_product_in_grid.cpp")
add_executable(P12 "${SRC_FOLDER1}P12_highly_divisible_triangle_number.cpp")
add_executable(P47 "${SRC_FOLDER1}P47_distinct_prime_factors.cpp")
add_executable(P50 "${SRC_FOLDER1}P50_consecutive_prime_sum.cpp")

set_property(GLOBAL PROPERTY CXX_STANDARD 20)