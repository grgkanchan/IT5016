# IT5016


class RequestSystem:
    _id_counter = 1000
    
  def __init__(self):
        self.requests = [] 

   def user_info(self, name, age):
        user_id = RequestSystem._id_counter
        RequestSystem._id_counter += 1
        # Generate reference number using last three letters of name and user ID
        last_three_letters = name[-3:] if len(name) >= 3 else name
        reference_number = f"{user_id}{last_three_letters.lower()}"
        return {
            "user_id": user_id,
            "name": name,
            "age": age,
            "reference_number": reference_number
        }

  def request_details(self, items_with_costs):
        total_amount = sum(cost for item, cost in items_with_costs)
        item_list = [item for item, cost in items_with_costs]
        return total_amount, item_list

  def request_approval(self, total_amount):
        return "approved" if total_amount < 150 else "pending"

  def respond_request(self, user_id, response):
        for request in self.requests:
            if request["user_id"] == user_id:
                if request["status"] == "pending":
                    request["status"] = response
                break

  def display_request(self):
        for request in self.requests:
            print("\nDetailed Report:")
            print(f"User Name: {request['name']}")
            print(f"Unique ID: {request['user_id']}")
            print(f"Total Amount: ${request['total_amount']:.2f}")
            print(f"Category: {request['status']}")
            print(f"Approval Reference Number: {request['reference_number']}")
            print("-" * 40)

  def request_statistic(self):
        total_requests = len(self.requests)
        approved_requests = sum(1 for request in self.requests if request["status"] == "approved")
        pending_requests = sum(1 for request in self.requests if request["status"] == "pending")
        not_approved_requests = sum(1 for request in self.requests if request["status"] == "not approved")

  print("\nRequest Statistics:")
        print(f"Total Requests Submitted: {total_requests}")
        print(f"Total Approved Requests: {approved_requests}")
        print(f"Total Pending Requests: {pending_requests}")
        print(f"Total Not Approved Requests: {not_approved_requests}")

   def add_request(self):

  explanation:
1.KISS (Keep It Simple, Stupid):
          Explanation: This principle suggests that code should be simple and easy to understand. Unnecessary complexity should be avoided.
          Application to the code.The code is mostly simple, especially in how it manages user requests, approvals, and statistics.
          However, the add_request method could be simplified. Currently, it calls multiple other methods (user_info, request_details, and request_approval) in sequence, which makes it slightly more complex than necessary.
          Some of the method names could be more self-explanatory. For example, respond_request might be better named as update_request_status for clarity.
2. DRY (Don't Repeat Yourself):
         Explanation: This principle encourages avoiding redundancy by not duplicating code, which can lead to maintenance issues.
         Application to the code:The code follows the DRY principle well,The methods (user_info, request_details, request_approval) each handle a specific task, which prevents code duplication.
         However, the logic to update the request status in respond_request could potentially be reused in other methods. Right now, it only checks if the request status is "pending" before updating, which could be extracted to a helper function for validation.
3. YAGNI (You Aren't Gonna Need It):
         Explanation: This principle suggests that you should not add functionality until it's necessary. Avoid over-engineering or anticipating features that may not be needed.
         Application to the code:The current code doesn't over-engineer or add unnecessary complexity. For example, it doesn't include extra fields or features that aren't required for handling requests.
          However, the user_info method includes parameters for age and email, even though they are not used when adding a request (age is set to 0, and email is empty). This could be simplified until such details are needed.
4. Single Responsibility Principle (SRP):
         Explanation: This principle states that a class or function should have one, and only one, reason to change. Each class or function should focus on a single responsibility.
         Application to the code:The RequestSystem class handles too many responsibilities like manages user information,calculates request details and costs,
                                 
  Summary:
    KISS: It is generally simple, though there are minor improvements that could simplify method names and flows.
    DRY: The code avoids repetition well but could further abstract some parts (e.g., updating request status).
    YAGNI: There’s a slight violation with unused user fields, but otherwise, the code stays lean and focused.
    SRP: This could be improved by breaking the RequestSystem class into smaller, more focused classes.
