# JSON CV Builder

def main():
  
    print("""
    Welcome to CV Builder.
    """)

    with open('resume.txt', 'r') as f:
        data = f.read()
        
    print(data)

if __name__ == "__main__":
    main()