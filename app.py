try:
    file = open("app.py")
    try:
        age = int(input("Age: "))
        xfactor = 10/age
        # file.close()
    except (ValueError, ZeroDivisionError):
        print("You didn't enter a valid age.")
    except Exception:
        print("Something went wrong...")
    else:
        print("No exceptions were thrown.")
    finally:
        file.close()
except Exception:
    print("Something went wrong:")

print("Execution continues.")
