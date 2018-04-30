import getopt, sys




def main():

    print ('Number of args is ', len (sys.argv))
    if ( len(sys.argv) == 1 ) :
        print ('In sufficient arguments, quitting !. Please pass in some arguments to continue processing. ')
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            print ( "In the verbose section of the code")
            verbose = True
        elif o in ("-h", "--help"):
            print ( "In the help section of the code")
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            print ( "In the output section of the code")
            output = a
        else:
            assert False, "unhandled option"
    # ...
def usage () :
	print ( "In the usage section of the code" )

if __name__ == "__main__":
    main()
