#ifndef EVALUATE_H_
#define EVALUATE_H_

#include <string>

bool is_valid_expression(const std::string& expression);
int evaluate_factor(std::string expression);
int evaluate_term(std::string expression);
int evaluate_expression(std::string expression);

#endif // EVALUATE_H