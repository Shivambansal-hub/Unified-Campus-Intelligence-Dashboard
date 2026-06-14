from datetime import date, timedelta
from models import MenuItem, Meal, DayMenu

# ── Weekly rotating menu with realistic Indian campus food ──

WEEKLY_MENU = {
    "Monday": {
        "breakfast": Meal(meal_type="breakfast", timing="7:30 AM – 9:30 AM", items=[
            MenuItem(id=1, name="Masala Dosa", price=30, is_veg=True, calories=250, description="Crispy rice crepe with spiced potato filling", allergens=["gluten"]),
            MenuItem(id=2, name="Idli Sambar", price=25, is_veg=True, calories=200, description="Steamed rice cakes with lentil soup"),
            MenuItem(id=3, name="Bread Omelette", price=35, is_veg=False, calories=320, description="Fluffy omelette on buttered toast", allergens=["eggs", "gluten"]),
            MenuItem(id=4, name="Poha", price=20, is_veg=True, calories=180, description="Flattened rice with peanuts and curry leaves"),
            MenuItem(id=5, name="Tea / Coffee", price=10, is_veg=True, calories=60, description="Hot beverage", allergens=["dairy"]),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:00 PM – 2:00 PM", items=[
            MenuItem(id=6, name="Rajma Chawal", price=50, is_veg=True, calories=450, description="Kidney bean curry with steamed rice"),
            MenuItem(id=7, name="Chicken Biryani", price=80, is_veg=False, calories=550, description="Fragrant basmati rice with spiced chicken", allergens=["dairy"]),
            MenuItem(id=8, name="Paneer Butter Masala", price=60, is_veg=True, calories=380, description="Cottage cheese in creamy tomato gravy", allergens=["dairy"]),
            MenuItem(id=9, name="Dal Tadka + Roti", price=40, is_veg=True, calories=350, description="Tempered lentils with whole wheat flatbread", allergens=["gluten"]),
            MenuItem(id=10, name="Green Salad", price=15, is_veg=True, calories=80, description="Fresh cucumber, tomato, and onion"),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=11, name="Chole Bhature", price=55, is_veg=True, calories=520, description="Spiced chickpeas with fried bread", allergens=["gluten"]),
            MenuItem(id=12, name="Egg Curry + Rice", price=50, is_veg=False, calories=420, description="Boiled eggs in tangy gravy with rice", allergens=["eggs"]),
            MenuItem(id=13, name="Aloo Gobi", price=40, is_veg=True, calories=280, description="Potato and cauliflower stir-fry"),
            MenuItem(id=14, name="Chapati (4 pcs)", price=20, is_veg=True, calories=320, description="Whole wheat flatbreads", allergens=["gluten"]),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=15, name="Samosa (2 pcs)", price=20, is_veg=True, calories=280, description="Crispy pastry with spiced potato filling", allergens=["gluten"]),
            MenuItem(id=16, name="Vada Pav", price=15, is_veg=True, calories=250, description="Spiced potato fritter in a bun", allergens=["gluten"]),
            MenuItem(id=17, name="Chai", price=10, is_veg=True, calories=80, description="Indian spiced tea", allergens=["dairy"]),
        ]),
    },
    "Tuesday": {
        "breakfast": Meal(meal_type="breakfast", timing="7:30 AM – 9:30 AM", items=[
            MenuItem(id=18, name="Aloo Paratha", price=35, is_veg=True, calories=300, description="Stuffed potato flatbread with curd", allergens=["gluten", "dairy"]),
            MenuItem(id=19, name="Upma", price=20, is_veg=True, calories=220, description="Semolina porridge with vegetables", allergens=["gluten"]),
            MenuItem(id=20, name="Boiled Eggs (2)", price=15, is_veg=False, calories=140, description="Farm-fresh boiled eggs", allergens=["eggs"]),
            MenuItem(id=21, name="Cornflakes + Milk", price=25, is_veg=True, calories=200, description="Crunchy cereal with cold milk", allergens=["dairy", "gluten"]),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:00 PM – 2:00 PM", items=[
            MenuItem(id=22, name="South Indian Thali", price=70, is_veg=True, calories=500, description="Rice, sambar, rasam, poriyal, curd, papad", allergens=["dairy"]),
            MenuItem(id=23, name="Fish Fry + Rice", price=90, is_veg=False, calories=480, description="Crispy fried fish with lemon rice", allergens=["fish"]),
            MenuItem(id=24, name="Matar Paneer + Naan", price=65, is_veg=True, calories=420, description="Peas and cottage cheese curry with naan", allergens=["dairy", "gluten"]),
            MenuItem(id=25, name="Mixed Veg Curry", price=40, is_veg=True, calories=280, description="Seasonal vegetables in mild curry"),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=26, name="Veg Fried Rice", price=45, is_veg=True, calories=380, description="Wok-tossed rice with vegetables"),
            MenuItem(id=27, name="Chicken Curry + Roti", price=70, is_veg=False, calories=480, description="Home-style chicken curry with flatbread", allergens=["gluten"]),
            MenuItem(id=28, name="Palak Dal", price=35, is_veg=True, calories=250, description="Spinach lentil soup"),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=29, name="Pav Bhaji", price=30, is_veg=True, calories=350, description="Spiced vegetable mash with buttered buns", allergens=["gluten", "dairy"]),
            MenuItem(id=30, name="Cold Coffee", price=25, is_veg=True, calories=180, description="Chilled coffee with ice cream", allergens=["dairy"]),
        ]),
    },
    "Wednesday": {
        "breakfast": Meal(meal_type="breakfast", timing="7:30 AM – 9:30 AM", items=[
            MenuItem(id=31, name="Puri Bhaji", price=30, is_veg=True, calories=350, description="Fried bread with potato curry", allergens=["gluten"]),
            MenuItem(id=32, name="Rava Dosa", price=30, is_veg=True, calories=230, description="Crispy semolina crepe", allergens=["gluten"]),
            MenuItem(id=33, name="Fruit Bowl", price=25, is_veg=True, calories=120, description="Seasonal fresh fruits"),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:00 PM – 2:00 PM", items=[
            MenuItem(id=34, name="Mutton Biryani", price=100, is_veg=False, calories=620, description="Aromatic rice layered with tender mutton", allergens=["dairy"], is_special=True),
            MenuItem(id=35, name="Dal Makhani + Rice", price=55, is_veg=True, calories=450, description="Creamy black lentils with steamed rice", allergens=["dairy"]),
            MenuItem(id=36, name="Kadhai Paneer", price=60, is_veg=True, calories=400, description="Paneer in bell pepper tomato gravy", allergens=["dairy"]),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=37, name="Pasta Arrabiata", price=55, is_veg=True, calories=380, description="Penne in spicy tomato sauce", allergens=["gluten"]),
            MenuItem(id=38, name="Butter Chicken + Naan", price=85, is_veg=False, calories=550, description="Creamy tomato chicken with naan", allergens=["dairy", "gluten"]),
            MenuItem(id=39, name="Baingan Bharta", price=35, is_veg=True, calories=220, description="Smoky roasted eggplant mash"),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=40, name="Bread Pakora", price=20, is_veg=True, calories=300, description="Batter-fried stuffed bread", allergens=["gluten"]),
            MenuItem(id=41, name="Mango Lassi", price=25, is_veg=True, calories=200, description="Sweet mango yogurt drink", allergens=["dairy"]),
        ]),
    },
    "Thursday": {
        "breakfast": Meal(meal_type="breakfast", timing="7:30 AM – 9:30 AM", items=[
            MenuItem(id=42, name="Chole Kulche", price=35, is_veg=True, calories=380, description="Chickpea curry with soft bread", allergens=["gluten"]),
            MenuItem(id=43, name="Medu Vada", price=25, is_veg=True, calories=260, description="Crispy lentil donuts with chutney"),
            MenuItem(id=44, name="French Toast", price=30, is_veg=False, calories=280, description="Egg-dipped toasted bread with syrup", allergens=["eggs", "gluten", "dairy"]),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:00 PM – 2:00 PM", items=[
            MenuItem(id=45, name="Veg Pulao + Raita", price=45, is_veg=True, calories=380, description="Fragrant vegetable rice with yogurt", allergens=["dairy"]),
            MenuItem(id=46, name="Egg Biryani", price=60, is_veg=False, calories=480, description="Spiced rice with boiled eggs", allergens=["eggs"]),
            MenuItem(id=47, name="Malai Kofta", price=65, is_veg=True, calories=450, description="Paneer-potato dumplings in cream sauce", allergens=["dairy"]),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=48, name="Chana Masala + Roti", price=40, is_veg=True, calories=380, description="Spiced chickpea curry with flatbread", allergens=["gluten"]),
            MenuItem(id=49, name="Grilled Chicken Sandwich", price=55, is_veg=False, calories=350, description="Grilled chicken with lettuce in toasted bread", allergens=["gluten"]),
            MenuItem(id=50, name="Mixed Dal + Rice", price=35, is_veg=True, calories=320, description="Blend of five lentils with steamed rice"),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=51, name="Momos (6 pcs)", price=40, is_veg=True, calories=240, description="Steamed vegetable dumplings", allergens=["gluten"], is_special=True),
            MenuItem(id=52, name="Masala Chai", price=10, is_veg=True, calories=80, description="Spiced Indian tea", allergens=["dairy"]),
        ]),
    },
    "Friday": {
        "breakfast": Meal(meal_type="breakfast", timing="7:30 AM – 9:30 AM", items=[
            MenuItem(id=53, name="Paneer Paratha", price=40, is_veg=True, calories=340, description="Cottage cheese stuffed flatbread", allergens=["gluten", "dairy"]),
            MenuItem(id=54, name="Dosa + Chutney", price=25, is_veg=True, calories=220, description="Plain rice crepe with coconut chutney"),
            MenuItem(id=55, name="Banana Shake", price=25, is_veg=True, calories=200, description="Fresh banana milkshake", allergens=["dairy"]),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:00 PM – 2:00 PM", items=[
            MenuItem(id=56, name="Special Friday Biryani", price=90, is_veg=False, calories=580, description="Chef's special biryani with raita", allergens=["dairy"], is_special=True),
            MenuItem(id=57, name="Veg Biryani", price=55, is_veg=True, calories=420, description="Fragrant vegetable biryani with raita", allergens=["dairy"]),
            MenuItem(id=58, name="Shahi Paneer", price=65, is_veg=True, calories=420, description="Rich paneer in cream-cashew gravy", allergens=["dairy", "nuts"]),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=59, name="Noodles (Veg/Chicken)", price=50, is_veg=True, calories=350, description="Stir-fried noodles with vegetables", allergens=["gluten"]),
            MenuItem(id=60, name="Tandoori Roti + Paneer Tikka", price=70, is_veg=True, calories=400, description="Clay oven bread with grilled paneer", allergens=["dairy", "gluten"]),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=61, name="Spring Rolls (4 pcs)", price=30, is_veg=True, calories=260, description="Crispy rolls with vegetable filling", allergens=["gluten"]),
            MenuItem(id=62, name="Fresh Lime Soda", price=15, is_veg=True, calories=60, description="Sweet or salty lime soda"),
        ]),
    },
    "Saturday": {
        "breakfast": Meal(meal_type="breakfast", timing="8:00 AM – 10:00 AM", items=[
            MenuItem(id=63, name="Weekend Special Pancakes", price=40, is_veg=True, calories=350, description="Fluffy pancakes with maple syrup", allergens=["gluten", "dairy", "eggs"], is_special=True),
            MenuItem(id=64, name="Poha Jalebi", price=30, is_veg=True, calories=380, description="Flattened rice with sweet jalebi", allergens=["gluten"]),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:00 PM – 2:00 PM", items=[
            MenuItem(id=65, name="Chole Rice", price=45, is_veg=True, calories=420, description="Chickpea curry with jeera rice"),
            MenuItem(id=66, name="Mutton Curry + Roti", price=95, is_veg=False, calories=520, description="Slow-cooked mutton in aromatic gravy", allergens=["gluten"]),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=67, name="Pizza Night - Margherita", price=80, is_veg=True, calories=450, description="Classic margherita pizza", allergens=["gluten", "dairy"], is_special=True),
            MenuItem(id=68, name="Pizza Night - Chicken Tikka", price=100, is_veg=False, calories=520, description="Indian-style chicken tikka pizza", allergens=["gluten", "dairy"]),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=69, name="Bhel Puri", price=20, is_veg=True, calories=200, description="Puffed rice chaat with chutneys"),
        ]),
    },
    "Sunday": {
        "breakfast": Meal(meal_type="breakfast", timing="8:30 AM – 10:30 AM", items=[
            MenuItem(id=70, name="Brunch Thali", price=60, is_veg=True, calories=500, description="Poori, halwa, chana, dahi", allergens=["gluten", "dairy"], is_special=True),
            MenuItem(id=71, name="Egg Bhurji + Pav", price=35, is_veg=False, calories=320, description="Scrambled eggs with buttered buns", allergens=["eggs", "gluten", "dairy"]),
        ]),
        "lunch": Meal(meal_type="lunch", timing="12:30 PM – 2:30 PM", items=[
            MenuItem(id=72, name="Sunday Special: Butter Chicken Thali", price=110, is_veg=False, calories=650, description="Butter chicken, naan, rice, dal, raita, gulab jamun", allergens=["dairy", "gluten"], is_special=True),
            MenuItem(id=73, name="Sunday Special: Paneer Thali", price=80, is_veg=True, calories=550, description="Shahi paneer, naan, rice, dal, raita, gulab jamun", allergens=["dairy", "gluten"], is_special=True),
        ]),
        "dinner": Meal(meal_type="dinner", timing="7:00 PM – 9:00 PM", items=[
            MenuItem(id=74, name="Maggi", price=20, is_veg=True, calories=300, description="Classic 2-minute noodles", allergens=["gluten"]),
            MenuItem(id=75, name="Bread Butter + Soup", price=30, is_veg=True, calories=250, description="Tomato soup with buttered bread", allergens=["gluten", "dairy"]),
        ]),
        "snacks": Meal(meal_type="snacks", timing="4:00 PM – 5:30 PM", items=[
            MenuItem(id=76, name="Aloo Tikki Chaat", price=25, is_veg=True, calories=280, description="Crispy potato patty with chutneys and curd", allergens=["dairy"]),
        ]),
    },
}

DAYS_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def _get_today_name():
    return date.today().strftime("%A")


def get_today_menu():
    day_name = _get_today_name()
    day_menu = WEEKLY_MENU.get(day_name, WEEKLY_MENU["Monday"])
    return {
        "day": day_name,
        "date": date.today().isoformat(),
        "meals": day_menu,
    }


def get_week_menu():
    result = []
    today = date.today()
    today_weekday = today.weekday()  # 0=Monday
    for i, day_name in enumerate(DAYS_ORDER):
        day_date = today + timedelta(days=i - today_weekday)
        day_menu = WEEKLY_MENU[day_name]
        result.append({
            "day": day_name,
            "date": day_date.isoformat(),
            "meals": day_menu,
        })
    return result


def get_meal(meal_type: str):
    day_name = _get_today_name()
    day_menu = WEEKLY_MENU.get(day_name, WEEKLY_MENU["Monday"])
    meal = day_menu.get(meal_type)
    if not meal:
        return None
    return {"day": day_name, "date": date.today().isoformat(), "meal": meal}


def get_specials():
    day_name = _get_today_name()
    day_menu = WEEKLY_MENU.get(day_name, WEEKLY_MENU["Monday"])
    specials = []
    for meal_type, meal in day_menu.items():
        for item in meal.items:
            if item.is_special:
                specials.append({"meal_type": meal_type, "timing": meal.timing, "item": item})
    return {"day": day_name, "date": date.today().isoformat(), "specials": specials}
