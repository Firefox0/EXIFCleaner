import argparse
import cleaner
import viewer
import fs


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    parser_exif_viewer = subparser.add_parser("view")
    parser_exif_viewer.add_argument("--path", "-p", type=str)
    parser_exif_viewer.add_argument("--directory", "-d", type=str)

    parser_exif_cleaner = subparser.add_parser("clean")
    parser_exif_cleaner.add_argument("--path", "-p", type=str)
    parser_exif_cleaner.add_argument("--directory", "-d", type=str)

    args = parser.parse_args()
    if args.command == "view":
        if args.path:
            tags = viewer.get_exif(args.path)
            viewer.print_exif(tags)
        elif args.directory:
            file_paths = fs.get_images(args.directory)
            tags = viewer.get_exifs(file_paths)
            viewer.print_exifs(tags)
    elif args.command == "clean":
        if args.path:
            cleaner.remove_metadata(args.path)
            print("Successfully removed the exif.")
        elif args.directory:
            file_paths = fs.get_images(args.directory)
            cleaner.remove_metadata_multiple(file_paths)
    else:
        parser.error("Invalid arguments.")


if __name__ == "__main__":
    main()
