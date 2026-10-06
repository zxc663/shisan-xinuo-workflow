"""命令行入口：python cli.py list"""
import notes


def main(argv):
    """argv[0]='list' -> 返回标题列表（打印并返回）。"""
    cmd = argv[0] if argv else "list"
    if cmd == "list":
        titles = notes.list_notes()
        for t in titles:
            print(t)
        return titles
    raise SystemExit("unknown cmd: %s" % cmd)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
