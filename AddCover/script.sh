for file in *; do
    type=$(file "$file")

    if echo "$type" | grep -q "MPEG"; then
        echo "$file is MP3"
        name=$file
        mv "$file" music.mp3
    elif echo "$type" | grep -q "JPEG"; then
        echo "$file is JPG"
        mv "$file" image.jpg
    fi
done
lame --ti image.jpg music.mp3 "$name"
echo $name
read -p "Press Enter to continue: "
rm image.jpg music.mp3

#Use JPG and MP3