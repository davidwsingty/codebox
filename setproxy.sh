
# This script is used to set the proxy in Linux distros which uses /etc/profile
# pass the value of $1 as the first positional parameter
# run this script with . ./setproxy.sh

FILENAME1=/etc/profile

if [[ -z $(grep "http_proxy=\"http://$1\"" $FILENAME1) ]]; then
    echo "http_proxy=\"http://$1\"" >> $FILENAME1
fi

if [[ -z $(grep "https_proxy=\"https://$1\"" $FILENAME1) ]]; then
    echo "https_proxy=\"https://$1\"" >> $FILENAME1
fi

if [[ -z $(grep "export http_proxy" $FILENAME1) ]]; then
    echo "export http_proxy" >> $FILENAME1
fi

if [[ -z $(grep "export https_proxy" $FILENAME1) ]]; then
    echo "export https_proxy" >> $FILENAME1
fi

. $FILENAME1


