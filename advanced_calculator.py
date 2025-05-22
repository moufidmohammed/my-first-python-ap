import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero / خطأ: لا يمكن القسمة على الصفر"
def power(x, y): return x ** y
def sqrt(x): return math.sqrt(x)
def percentage(x, y): return (x / y) * 100
def modulo(x, y): return x % y

# اختر اللغة / Choose language
lang = input("اختر اللغة (ar = العربية / en = English): ")

if lang == "ar":
    print("مرحباً بك في الآلة الحاسبة المتقدمة")
    print("العمليات المتاحة:")
    print("1. جمع")
    print("2. طرح")
    print("3. ضرب")
    print("4. قسمة")
    print("5. أس (x^y)")
    print("6. الجذر التربيعي")
    print("7. النسبة المئوية (x من y)")
    print("8. باقي القسمة (mod)")

    choice = input("اختر العملية (1-8): ")

elif lang == "en":
    print("Welcome to the advanced calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Percentage (x of y)")
    print("8. Modulo (remainder)")

    choice = input("Choose operation (1-8): ")

else:
    print("Invalid language / لغة غير صالحة")
    exit()

# عمليات تتطلب رقم واحد
if choice == '6':
    num = float(input("Enter the number / أدخل الرقم: "))
    print("Result / النتيجة:", sqrt(num))

# العمليات الثنائية
else:
    num1 = float(input("Enter first number / أدخل الرقم الأول: "))
    num2 = float(input("Enter second number / أدخل الرقم الثاني: "))

    if choice == '1':
        print("Result / النتيجة:", add(num1, num2))
    elif choice == '2':
        print("Result / النتيجة:", subtract(num1, num2))
    elif choice == '3':
        print("Result / النتيجة:", multiply(num1, num2))
    elif choice == '4':
        print("Result / النتيجة:", divide(num1, num2))
    elif choice == '5':
        print("Result / النتيجة:", power(num1, num2))
    elif choice == '7':
        print("Result / النتيجة:", percentage(num1, num2), "%")
    elif choice == '8':
        print("Result / النتيجة:", modulo(num1, num2))
    else:
        print("اختيار غير صالح / Invalid choice")
