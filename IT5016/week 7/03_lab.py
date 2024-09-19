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