#!/bin/bash
#
# Tic Tac Toe
#
# 6 Jan 2018
# K. Strotz
#

dispRowOneColOne () {
    case $1 in
        "0")
            echo -n " ___|"
            ;;
        "1")
            echo -n " _X_|"
            ;;
        "2")
            echo -n " _O_|"
            ;;
        *)
            ;;
    esac
}

dispRowOneColTwo () {
    case $1 in
       "0")
           echo -n "___|"
           ;;
       "1")
           echo -n "_X_|"
           ;;
       "2")
           echo -n "_O_|"
           ;;
       *)
           ;;
    esac
}

dispRowOneColThree () {
    case $1 in
       "0")
           echo "___"
           ;;
       "1")
           echo "_X_"
           ;;
       "2")
           echo "_O_"
           ;;
       *)
           ;;
    esac
}

dispRowTwoColOne () {
    case $1 in
        "0")
            echo -n " ___|"
            ;;
        "1")
            echo -n " _X_|"
            ;;
        "2")
            echo -n " _O_|"
            ;;
        *)
            ;;
    esac
}

dispRowTwoColTwo () {
    case $1 in
       "0")
           echo -n "___|"
           ;;
       "1")
           echo -n "_X_|"
           ;;
       "2")
           echo -n "_O_|"
           ;;
       *)
           ;;
    esac
}

dispRowTwoColThree () {
    case $1 in
       "0")
           echo "___"
           ;;
       "1")
           echo "_X_"
           ;;
       "2")
           echo "_O_"
           ;;
       *)
           ;;
    esac
}

dispRowThreeColOne () {
    case $1 in
        "0")
            echo -n "    |"
            ;;
        "1")
            echo -n "  X |"
            ;;
        "2")
            echo -n "  O |"
            ;;
        *)
            ;;
    esac
}

dispRowThreeColTwo () {
    case $1 in
       "0")
           echo -n "   |"
           ;;
       "1")
           echo -n " X |"
           ;;
       "2")
           echo -n " O |"
           ;;
       *)
           ;;
    esac
}

dispRowThreeColThree () {
    case $1 in
       "0")
           echo "   "
           ;;
       "1")
           echo " X "
           ;;
       "2")
           echo " O "
           ;;
       *)
           ;;
    esac
}

dispBoard () {

echo ""
dispRowOneColOne $1 
dispRowOneColTwo $2
dispRowOneColThree $3
dispRowTwoColOne $4
dispRowTwoColTwo $5
dispRowTwoColThree $6
dispRowThreeColOne $7
dispRowThreeColTwo $8
dispRowThreeColThree $9

}

checkWin () {

if [ $tl == $tm ] && [ $tm == $tr ] && [ $tr != 0 ]; then
winFlag=1
elif [ $ml == $mm ] && [ $mm == $mr ] && [ $mr != 0 ]; then
winFlag=1
elif [ $bl == $bm ] && [ $bm == $br ] && [ $br != 0 ]; then
winFlag=1
elif [ $tl == $ml ] && [ $ml == $bl ] && [ $bl != 0 ]; then
winFlag=1
elif [ $tm == $mm ] && [ $mm == $bm ] && [ $bm != 0 ]; then
winFlag=1
elif [ $tr == $mr ] && [ $mr == $br ] && [ $br != 0 ]; then
winFlag=1
elif [ $tl == $mm ] && [ $mm == $br ] && [ $br != 0 ]; then
winFlag=1
elif [ $tr == $mm ] && [ $mm == $bl ] && [ $bl != 0 ]; then
winFlag=1
else
winFlag=0
fi

}

checkDraw () {

if [ $tl != 0 ] && [ $tm != 0 ] && [ $tr != 0 ] && 
[ $ml != 0 ] && [ $mm != 0  ] && [ $mr != 0 ] && 
[ $bl != 0 ] && [ $bm != 0 ] && [ $br != 0 ]; then
drawFlag=1
else
drawFlag=0
fi

}

drawFlag=0
winFlag=0
playerFlag=0
tl=0
tm=0
tr=0
ml=0
mm=0
mr=0
bl=0
bm=0
br=0

clear
echo ""
echo "Welcome to Tic-Tac-Toe!"
echo -n "Would you like to play as X or O: "
read teamChoice

while true; do
case $teamChoice in
    [Xx])
        echo ""
        echo "Setting player one as X...DONE."
        echo "Launching game..."
        sleep 2
        break
        ;;
    [Oo])
        echo ""
        echo "Setting player one as O...DONE."
        echo "Launching game..."
        playerFlag=1
        sleep 2
        break
        ;;
    *) 
        echo -n "Please enter a valid choice: "
        read teamChoice
esac
done

clear
echo ""
dispBoard $tl $tm $tr $ml $mm $mr $bl $bm $br
echo ""

while [ $winFlag == 0 ] && [ $drawFlag == 0 ]; do
if [ $playerFlag == 0 ]; then
echo "Player X"
else
echo "Player O"
fi

echo "Moves are row/column abbreviations."
echo -n "Please enter a move: "
read playerInput

if [ $playerFlag == 0 ]; then
case $playerInput in
    "tl")
        tl=1
        ;;
    "tm")
        tm=1
        ;;
    "tr")
        tr=1
        ;;
    "ml")
        ml=1
        ;;
    "mm")
        mm=1
        ;;
    "mr")
        mr=1
        ;;
    "bl")
        bl=1
        ;;
    "bm")
        bm=1
        ;;
    "br")
        br=1
        ;;
    *)       
        echo "Invalid move! Exiting game...DONE."
        sleep 1
        clear
        exit
        ;;
esac
else
case $playerInput in
    "tl")
        tl=2
        ;;
    "tm")
        tm=2
        ;;
    "tr")
        tr=2
        ;;
    "ml")
        ml=2
        ;;
    "mm")
        mm=2
        ;;
    "mr")
        mr=2
        ;;
    "bl")
        bl=2
        ;;
    "bm")
        bm=2
        ;;
    "br")
        br=2
        ;;
    *)
        echo "Invalid move! Exiting game...DONE."
        sleep 1
        clear
        exit
        ;;
esac

fi

clear
echo ""
dispBoard $tl $tm $tr $ml $mm $mr $bl $bm $br
echo ""

if [ $playerFlag == 0 ]; then
playerFlag=1
else
playerFlag=0
fi
checkWin
checkDraw
done
echo "Game complete! Thanks for playing!"
echo "Press ENTER to exit."

read userExit
clear
