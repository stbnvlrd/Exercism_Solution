class SimpleCalculator
    ALLOWED_OPERATIONS = ['+', '/', '*'].freeze
    class UnsupportedOperation < StandardError; end
  
    def self.calculate(first_operand, second_operand, operation)
      begin
        if operation == '+'
          solution = first_operand + second_operand
        elsif operation == '/' and second_operand
          solution = first_operand / second_operand
        elsif operation == '*'
          solution = first_operand * second_operand
        else
          raise SimpleCalculator::UnsupportedOperation
        end
      rescue ZeroDivisionError
        return "Division by zero is not allowed."
      rescue TypeError
        raise ArgumentError.new("Something went wrong!")
       
      end
    result = first_operand.to_s + " " + operation + " " + second_operand.to_s + " = " + solution.to_s
    return result
    end
  end
  