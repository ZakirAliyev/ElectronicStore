class ElectronicStore:
    def __init__(self):
        self.products = {}
        self.users = {}
        self.shopping_cart = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Bu istifadəçi adı artıq istifadə olunur.")
            return
        self.users[username] = password
        print("Qeydiyyat uğurla tamamlandı.")

    def login(self, username, password, user_type):
        if user_type == "admin":
            if username == "Tahir" and password == "123":
                print("Admin girişi uğurla tamamlandı")
                return True
            else:
                print("Admin istifadəçi adı və ya parol səhvdir.")
                return False
        elif user_type == "user":
            if username in self.users and self.users[username] == password:
                print("İstifadəçi girişi uğurla tamamlandı.")
                return True
            else:
                print("İstifadəçi adı və ya parol səhvdir.")
                return False
        else:
            print("İstifadəçi növü yalnışdır.")
            return False

    def admin_panel(self):
        while True:
            print("Admin Paneli")
            print("1. Məhsul əlavə et")
            print("2. Məhsulu sil")
            print("3. Məhsul sayını göstər")
            print("4. Məhsulun adını dəyişdir")
            print("5. Məhsulun qiymətini dəyişdir")
            print("6. Məhsulları göstər")
            print("7. Çıxış")
            choice = input("Seçiminizi edin (1-7): ")
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.delete_product()
            elif choice == "3":
                self.count_products()
            elif choice == "4":
                self.update_product_name()
            elif choice == "5":
                self.update_product_price()
            elif choice == "6":
                self.list_products()
            elif choice == "7":
                break
            else:
                print("Seçim yalnışdır.")

    def add_product(self):
        product_id = input("Məhsul ID'si: ")
        if product_id in self.products:
            quantity = int(input("Məhsul miqdarını daxil edin: "))
            self.products[product_id]["quantity"] += quantity
            print("Məhsul miqdarı yeniləndi.")
        else:
            product_name = input("Məhsulun adı: ")
            quantity = int(input("Məhsulun sayı: "))
            price = float(input("Məhsulun qiyməti: "))
            if price >= 0:
                self.products[product_id] = {"name": product_name, "quantity": quantity, "price": price}
                print("Məhsul uğurla əlavə olundu.")
            else:
                print("Qiymət yalnışdır.")

    def delete_product(self):
        product_id = input("Silmək istədiyiniz məhsulun ID'sini daxil edin: ")
        if product_id in self.products:
            current_quantity = self.products[product_id]["quantity"]
            quantity_to_delete = int(input("Silmək istədiyiniz məhsulun miqdarını daxil edin: "))
            if quantity_to_delete > current_quantity:
                print("Mağazada bu qədər məhsul qalmayıb.")
            else:
                self.products[product_id]["quantity"] -= quantity_to_delete
                print("Məhsul miqdarı uğurla yeniləndi.")
                if self.products[product_id]["quantity"] == 0:
                    print("Məhsul anbarda tükənib.")
        else:
            print("Bu ID ilə məhsul tapılmadı.")

    def count_products(self):
        total_quantity = sum([product["quantity"] for product in self.products.values()])
        print("Ümumi mıhsul sayı: {}".format(total_quantity))

    def update_product_name(self):
        product_id = input("Adını dəyişdirmək istədiyiniz məhsulun ID-sini daxil edin: ")
        if product_id in self.products:
            new_name = input("Yeni məhsul adı: ")
            self.products[product_id]["name"] = new_name
            print("Məhsulun adı uğurla yeniləndi.")
        else:
            print("Bu ID ilə məhsul tapılmadı.")

    def update_product_price(self):
        product_id = input("Qiymətini dəyişmək istədiyiniz məhsulun ID-sini daxil edin: ")
        if product_id in self.products:
            new_price = float(input("Yeni məhsulun qiyməti: "))
            if new_price >= 0:
                self.products[product_id]["price"] = new_price
                print("Məhsulun qiyməti uğurla yeniləndi.")
            else:
                print("Qiymət yalnışdır.")
        else:
            print("Bu ID ilə məhsul tapılmadı.")

    def list_products(self):
        print("Mövcud məhsullar: ")
        for product_id, product_info in self.products.items():
            print("ID: {}, Adı: {}, Sayı: {}, Qiyməti: {}".format(
                product_id, product_info["name"], product_info["quantity"], product_info["price"]
            ))

    def update_cart_quantities(self):
        for product_id, cart_item in self.shopping_cart.items():
            if product_id in self.products:
                self.products[product_id]["quantity"] -= cart_item["quantity"]
                if self.products[product_id]["quantity"] == 0:
                    print("Məhsul anbarda tükənib.")
            else:
                print("Bu ID ilə məhsul tapılmadı.")

    def add_to_cart(self, product_id, quantity):
        if product_id in self.products:
            if quantity <= self.products[product_id]["quantity"]:
                if product_id in self.shopping_cart:
                    self.shopping_cart[product_id]["quantity"] += quantity
                else:
                    self.shopping_cart[product_id] = {
                        "name": self.products[product_id]["name"],
                        "quantity": quantity,
                        "price": self.products[product_id]["price"]
                    }
                print("Məhsul səbətə əlavə edildi.")
                self.products[product_id]["quantity"] -= quantity
            else:
                print("Mağazada bu sayda məhsul qalmayıb.")
        else:
            print("Bu ID ilə məhsul tapılmadı.")

    def view_cart(self):
        if not self.shopping_cart:
            print("Sizin səbətiniz boşdur.")
        else:
            total_price = 0
            print("Səbətinizdəki məhsullar:")
            for product_id, cart_item in self.shopping_cart.items():
                print("ID: {}, Adı: {}, Miqdarı: {}, Qiyməti: {}".format(
                    product_id, cart_item["name"], cart_item["quantity"], cart_item["price"]
                ))
                total_price += cart_item["quantity"] * cart_item["price"]
            print("Ümumi miqdar: {}".format(total_price))

    def clear_cart(self):
        if not self.shopping_cart:
            print("Səbətiniz tamamilə boşdur.")
            return

        for product_id, cart_item in self.shopping_cart.items():
            if product_id in self.products:
                self.products[product_id]["quantity"] += cart_item["quantity"]

        self.shopping_cart = {}
        print("Səbətiniz boşaldıldı.")

    def get_products(self):
        if not self.shopping_cart:
            print("Səbətiniz tamamilə boşdur.")
            return

        self.shopping_cart = {}
        print("Məhsullar uğurla alındı və səbətiniz boşaldıldı.")


store = ElectronicStore()

store.products = {
    "1": {"name": "Noutbuk", "quantity": 5, "price": 2500.0},
    "2": {"name": "Smartfon", "quantity": 10, "price": 1500.0},
    "3": {"name": "Televizor", "quantity": 3, "price": 3000.0},
    "4": {"name": "Qulaqlıq", "quantity": 8, "price": 100.0},
    "5": {"name": "Planşet", "quantity": 2, "price": 800.0}
}

while True:
    print("1. Qeydiyyat")
    print("2. Daxil ol")
    print("3. Çıxış")
    choice = input("Seçiminizi edin (1-3): ")

    if choice == "1":
        username = input("İstifadəçi adı: ")
        password = input("Şifrə: ")
        store.register_user(username, password)
    elif choice == "2":
        print("1. Admin Girişi")
        print("2. İstifadəçi Girişi")
        user_choice = input("Seçiminizi edin (1-2): ")
        if user_choice == "1":
            username = input("İstifadəçi adı: ")
            password = input("Şifrə: ")
            if store.login(username, password, "admin"):
                store.admin_panel()
        elif user_choice == "2":
            username = input("İstifadəçi adı: ")
            password = input("Şifrə: ")
            if store.login(username, password, "user"):
                while True:
                    print("1. Məhsulu səbətə əlavə et")
                    print("2. Səbəti göstər")
                    print("3. Səbəti boşalt")
                    print("4. Məhsulları al")
                    print("5. Çıxış")
                    user_choice = input("Seçiminizi edin (1-5): ")
                    if user_choice == "1":
                        store.list_products()
                        product_id = input("Məhsul ID'si: ")
                        quantity = int(input("Məhsul miqdarı: "))
                        store.add_to_cart(product_id, quantity)
                    elif user_choice == "2":
                        store.view_cart()
                    elif user_choice == "3":
                        store.clear_cart()
                    elif user_choice == "4":
                        store.get_products()
                    elif user_choice == "5":
                        break
                    else:
                        print("Seçim yalnışdır.")
        else:
            print("Seçim yalnışdır.")
    elif choice == "3":
        break
    else:
        print("Seçim yalnışdır.")
