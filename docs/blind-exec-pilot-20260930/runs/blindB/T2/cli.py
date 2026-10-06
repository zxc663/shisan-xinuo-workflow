"""命令行入口：python cli.py list [--tag <标签>]"""
import notes


def main(argv):
    """argv[0]='list' -> 返回标题列表（打印并返回）；支持 --tag <标签> 过滤。"""
    cmd = argv[0] if argv else "list"
    if cmd == "list":
        args = argv[1:]
        tag = None
        if "--tag" in args:
            i = args.index("--tag")
            if i + 1 >= len(args):
                raise SystemExit("--tag requires a value")
            tag = args[i + 1]
        titles = notes.list_notes(tag=tag)
        for t in titles:
            print(t)
        return titles
    raise SystemExit("unknown cmd: %s" % cmd)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
