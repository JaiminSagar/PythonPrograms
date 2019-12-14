#First Install external module 'patool' form pip --> pip install patool
import patoolib

print("Welcome! to our Create/Extract ZIP (Archive File) Program.")
print()
ans = 'No'
while ans.title() == 'No':
    s = input("\tWhat do want to do(Extract/Create):")
    if s.title() == "Create":
        n = int(input("\n\tHow many file do you want to Attach? : "))
        files = []
        for i in range(n):
            print("\tEnter File", i+1, "name with Extension:", end=" ")
            files.append(input())
        archFile = input("\n\tEnter Archive File Name with Extension(.zip):")
        patoolib.create_archive(archFile, tuple(files))

    elif s.title() == "Extract":
        ExFileName = input("\n\tEnter Archive File Name with Extension(.zip):")
        patoolib.extract_archive(ExFileName)
    else:
        print("\n\tEnter Valid option Name.....")

    ans = input("\n\tDo You Exit Program? (Yes/No): ")







