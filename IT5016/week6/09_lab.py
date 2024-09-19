class Movie:
    def __init__(self,title,genre,year):
        self.title = title 
        self.genre = genre
        self.year = year 
        self.available = True
        
    def mark_as_rented(self):
        self.available = False
        
    def mark_as_available(self):
        self.available = True
        
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - {'Available' if self.available else'rented'}" 
       
class Customer:
    def _init_(self, name):
        self.name = name
        self.rented_movies=[]
      
    def rent_movie(self,movie):
        if movie.available:
            movie.mark_as_rented()
            self.rented_movies.append(movie)
            print(f"{self.name} rented {movie.title}")
            
        else:
            print(f"{movie.title} is not available")
            
    def return_movie(self,movie):
        if movie in self.rented_movies:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} returned {movie.title}")
        else:
            print(f"{self.name} did not rent {movie.title}")
            
    def list_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies:")
            for movie in self.rented_movies:
                print(movie)
        else:
            print(f"{self.name} has no rented movies.")   
            
class Rentalstore:
    def ___init___(self):
        self.movies = []
        
    def add_movie(self,movie):
        self.movies.append(movie)
        
    def list_movies(self):
        if self.movies:
            print("Available Movies:")
            for movie in self.movies:
                print(movie)
        else:
            print("No movies available.")
            
    def find_movie(self,title):
        for movie in self.movies:
                if movie.title.lower() == title.lower():
                    return movie
        return None
    
def menu():
    print("\nMovie Rental System Menu")
    print("1. list Available Movies")   
    print("2. rent a Movie")
    print("3. Return a Movie")
    print("4. List Rented Movies")
    print("5.Add a Movie to Store")
    print("6. Exit")
        
def main():
        #initialize the store and movies
    store = Rentalstore()
    store.add_movie(Movie("Inception","Sci-Fi",2010))
    store.add_movie(Movie("The Matrix","Action",1999))
    store.add_movie(Movie("The Godfather","Crime",1972))
        
        #Initialize customers
    Customers = {
        "Alice": Customer("Alice"),
        "Bob": Customers("Bob")
    }
        
    while True:
            menu()
            choice = input("Enter your choice:").strip()
            
            if choice == "1":
                store.list_movies()
            elif choice == "2":
                customer_name = input("Enter your name:").strip()
                movie_title = input("Enter movie title to rent:").strip()
                Customer = Customers.get(customer_name)
                movie = store.find_movie(movie_title)
                if Customer and movie:
                    Customer.rent_movie(movie)
                elif not Customer:
                  print("Customer not found.")
                elif not movie:
                  print("Movie not found")
            elif choice == "3":
                Customer_name = input("Enter your name:").strip()
                movie_title = input("Enter your title to return:").strip()
                Customer = Customers.get(Customer_name)
                movie = store.find_movie(movie)
                if Customer and movie:
                    Customer.return_movie(movie)
                elif not Customer:
                    print("Customer not found")
                elif not movie:
                    print("Movie not found")
            elif choice == "4":
                Customer_name = input("Enter your name:").strip()
                Customers = Customers.get(Customer_name)
                if Customer:
                    Customer.list_rented_movies()
                else:
                    print("Customer not found.")
            elif choice == "5":
                title = input("Enter movie title: ").strip()
                genre = input("Enter movie grnre: ").strip()
                year = int(input("Enter movie year:")).strip()
                store.add_movie(movie(title,genre,year))
            elif  choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
                
if __name__ == "__main__":
   main()   
            
                
                
                        
                        
                        
                    
                    
                   
                        
        
        
        
            
        
        
        
        
        
        
                           
            
                    
                                 
            
            
                          
            