module SavingsAccount
  def self.interest_rate(balance)
    if balance < 0 then
      return -3.213
    elsif balance < 1000 then
      return 0.5
    elsif balance < 5000 then
      return 1.621
    elsif balance >= 5000 then
      return 2.475
    else
      raise "Error in interest rate"
    end
  end
  
  def self.annual_balance_update(balance)
    interest = (self.interest_rate(balance)).abs
    return balance*(1+(interest/100))
  end
  
  def self.years_before_desired_balance(current_balance, desired_balance)
    raise 'Please implement the SavingsAccount.years_before_desired_balance method'
  end
end
  