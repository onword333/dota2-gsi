from overlay.overlay import OverlayApp


def main():
    # current_time = 350
    # gold_rune = GoldRune()
    # wisdom_rune = WisdomRune()

    # msg = f'{gold_rune.name}: {gold_rune.time_until_next_appearance(current_time)}\n'
    # msg += f'{wisdom_rune.name}: {wisdom_rune.time_until_next_appearance(current_time)}'

    #print(msg)


    app = OverlayApp()
    app.mainloop()


if __name__ == "__main__":
    main()
