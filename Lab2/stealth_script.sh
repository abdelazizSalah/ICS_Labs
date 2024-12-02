while true; do
    sudo raw_packet eth1 02:42:0a:0a:16:02 0x0806 payLoadAlice.bin
    sudo raw_packet eth1 02:42:0a:0a:16:03 0x0806 payLoadBob.bin
    sleep 1
done