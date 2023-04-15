cmake_minimum_required (VERSION 3.8)

project ("EulerProblems")

add_executable(P4 P4_largest_palindrome.cpp)

add_executable(P5 P5_smallest_multiple.cpp)

add_executable(P6 P6_sum_square_difference.cpp)

add_executable(P7 P7_10001st_prime.cpp)

add_executable(P8 P8_largest_product_in_a_series)

add_executable(P9 P9_special_pythagorean_triplet.cpp)

add_executable(P10 P10_summation_of_primes.cpp)

add_executable(P11 P11_largest_product_in_grid.cpp)

add_executable(P12 P12_highly_divisible_triangle_number.cpp)

add_executable(P47 P47_distinct_prime_factors.cpp)

add_executable(P50 P50_consecutive_prime_sum.cpp)

set_property(GLOBAL PROPERTY CXX_STANDARD 20)