from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    varastoinfo(mehua, olutta)

    mehun_lisays_ja_ottaminen(mehua)

    virhetilanteet()

    print("mehua.lisaa_varastoon(-666.0)")

    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\nOlutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")

    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\nOlutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)")

    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\nMehuvarasto: {mehua}")

def varastoinfo(mehua, olutta):
    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto:{olutta}")
    print(f"Olut getterit:\nsaldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehun_lisays_ja_ottaminen(mehua):
    print("Mehu setterit:\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteet():
    print("Virhetilanteita:\nVarasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def lisaykset(olutta, mehua):
    print(f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\nMehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")

    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\nOlutvarasto: {olutta}")


if __name__ == "__main__":
    main()
