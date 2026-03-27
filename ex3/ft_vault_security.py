def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    try:
        with open("classified_data.txt", "r") as vault1:
            print("SECURE EXTRACTION:")
            content = vault1.read()
            lines = content.splitlines()
            for line in lines:
                print(line)
            raise Exception("test crash!")

    except Exception:
        pass
    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as vault2:
        vault2.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")
    if vault1.closed and vault2.closed:
        print("Vault automatically sealed upon completion")
    else:
        print("ERROR: a vault is still open!")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
