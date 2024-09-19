class RequestSystem:
    _id_counter = 1

    def __init__(self):
        self.requests = [] 

    def user_info(self, name, age, email):
        user_id = RequestSystem._id_counter
        RequestSystem._id_counter += 1
        return {
            "user_id": user_id,
            "name": name,
            "age": age,
            "email": email
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
            print(f"User ID: {request['user_id']}")
            print(f"Name: {request['name']}")
            print(f"Total Amount: ${request['total_amount']:.2f}")
            print(f"Status: {request['status']}")
            print("-" * 40)

    def request_statistic(self):
        total_requests = len(self.requests)
        approved_requests = sum(1 for request in self.requests if request["status"] == "approved")
        pending_requests = sum(1 for request in self.requests if request["status"] == "pending")
        not_approved_requests = sum(1 for request in self.requests if request["status"] == "not approved")

        print(f"Total Requests Submitted: {total_requests}")
        print(f"Total Approved Requests: {approved_requests}")
        print(f"Total Pending Requests: {pending_requests}")
        print(f"Total Not Approved Requests: {not_approved_requests}")

    def add_request(self, name, items_with_costs):
        user_info = self.user_info(name, 0, "")
        total_amount, item_list = self.request_details(items_with_costs)
        status = self.request_approval(total_amount)
        request = {
            "user_id": user_info["user_id"],
            "name": user_info["name"],
            "total_amount": total_amount,
            "status": status
        }
        self.requests.append(request)

if __name__ == "__main__":
    system = RequestSystem()

    system.add_request("ruhan", [("Laptop", 1200), ("Mouse", 30)])
    system.add_request("kanchan", [("Keyboard", 70), ("Headphones", 45)])
    system.display_request()
    system.respond_request(1, "not approved")
    system.request_statistic()

