import subprocess


#    NOTES
#
# 1. Usually this is 1500 by default.
# 2. If you use a VPN (especially OpenVPN or WireGuard), bet less:
# * `1400 ' — safe value
# * '1380 — - for OpenVPN (especially over TCP)
# * `1280 ' — for IPv6 / unstable connection
#
#

def test_ping(size, host="ya.ru"):
    try:
        result = subprocess.run(
            ["ping", host, "-f", "-l", str(size)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output = result.stdout.lower()
        return (
            "требуется фрагментация" not in output and "request timed out" not in output
        )
    except Exception as e:
        print(f"Ошибка: {e}")
        return False


def find_max_mtu(host="ya.ru", start=1472, min_size=1200):
    print(f"🔍 Подбор MTU для {host}. Уменьшаем размер...")

    mtu = start
    last_success = None

    while mtu >= min_size:
        print(f"Проверка: {mtu} байт...", end=" ")
        if test_ping(mtu, host):
            print("✅ OK")
            last_success = mtu
            mtu -= 1
        else:
            print("❌ Ошибка фрагментации")
            break

    if last_success:
        final_mtu = last_success + 28
        print(f"\n🎯 Максимальный рабочий размер данных: {last_success}")
        print(f"📏 Рекомендуемое значение MTU: {final_mtu}")
        return final_mtu
    else:
        print("❗ Не найдено подходящего значения.")
        return None


if __name__ == "__main__":
    find_max_mtu()
