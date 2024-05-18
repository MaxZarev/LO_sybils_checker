def main():
    print("Запускаем проверку на сибилов...")

    with open("L0_sybils.txt", "r") as file:
        wallets_sybils = file.read().splitlines()

    wallets_sybils = [wallet.lower() for wallet in wallets_sybils]


    print(f"В базе данных сиббилов: {len(wallets_sybils)} кошельков")

    with open("wallets.txt", "r") as file:
        wallets = file.read().splitlines()

    print(f"На проверку добавлено: {len(wallets)} кошельков")

    wallets = [wallet.lower() for wallet in wallets]

    sybils_detected = []

    for num, wallet in enumerate(wallets):
        if wallet in wallets_sybils:
            sybils_detected.append(wallet)
            print(f"Cибил обнаружен, кошелек {num}: {wallet}")

    print(f"Всего помечено сибиллом: {len(sybils_detected)}")

    with open("sybils_detected.txt", "w") as file:
        for wallet in sybils_detected:
            file.write(wallet + "\n")
    print("Скрипт подготовлен: https://t.me/maxzarev")


if __name__ == "__main__":
    main()
