import items
import monsters


def start():
    playing = True

    count = 0
    rarities = {}
    got = False
    while 1:
        drops = items.item_drop()
        for item in drops:
            print item
            if item["name"] == "Deimos":
                got = True

        if got:
            break


        count += 1

    print count

if __name__ == "__main__":
    start()
