# Session Context — YouTube MP3 Downloads

## Completed Task
- Session 1: Downloaded 2 YouTube URLs as MP3 with embedded thumbnails and ID3 tags.
- Session 2: Downloaded 9 YouTube URLs as MP3 with embedded thumbnails and ID3 tags.
- Session 3: Downloaded 1 YouTube URL as MP3 with embedded thumbnail and ID3 tags.
- Session 4: Downloaded 1 YouTube URL as MP3 with embedded thumbnail and ID3 tags.
- Session 5: Downloaded 1 YouTube URL as MP3 with embedded thumbnail and ID3 tags.
- Session 6: Downloaded 3 YouTube URLs as MP3 with embedded thumbnails and ID3 tags (Chhichhore soundtrack).
- Session 7: Downloaded 1 YouTube URL as MP3 with embedded thumbnail and ID3 tags.
- Session 8: Downloaded 9 YouTube URLs as MP3 with embedded thumbnails and ID3 tags (2 trimmed: silence removal, first 10s removal). 1 URL unavailable.
- Session 9: Restored context on CachyOS (OS reinstall). Verified toolchain: system `yt-dlp` 2026.10.21 + ffmpeg n9.0.2; full download/thumbnail/metadata pipeline tested OK.
- Session 10: Downloaded 26 unique YouTube URLs (27 given, 1 duplicate) as MP3 with embedded thumbnails and cleaned ID3 tags.
- Session 11: Downloaded 34 YouTube URLs as MP3 with embedded thumbnails and cleaned ID3 tags. 1 URL unavailable (Free Bird).
- Session 12: Downloaded 3 YouTube URLs as MP3 with embedded thumbnails and cleaned ID3 tags (Pardesiya kept as a second version).
- Session 13: Downloaded 16 YouTube URLs as MP3 with embedded thumbnails and cleaned ID3 tags. 1 duplicate skipped (The Lazy Song); Blue loop replaced with normal version.
- Session 14: Downloaded 1 YouTube URL (Cupid official MV); replaced the looped lyric version.

## Tools Used
- **yt-dlp** 2026.10.21 (`/usr/bin/yt-dlp`, installed via pacman) — works out of the box, no node/deno required
- **ffmpeg** n9.0.2 (`/usr/bin/ffmpeg`)
- **lame** (`/usr/bin/lame`) — used by `script.sh` for cover-art embedding

> **Environment note (Session 9):** Old OS was replaced with CachyOS. The old `~/bin/yt-dlp` and `~/.local/bin/yt-dlp` binaries are gone — use the system `yt-dlp` on PATH. Commands below are updated accordingly.

## Input URLs

| # | URL | Notes |
|---|-----|-------|
| 1 | `https://youtu.be/iKnqjtLeWmg?si=9xLMeI0UBvt0dtMa` | Used its own thumbnail |
| 2 | `https://youtu.be/ZRtdQ81jPUQ?si=vVB5JX4tbX6dK9eu` | Used thumbnail from URL 3 |
| 3 | `https://youtu.be/PgBvV9ofjmA?si=QZQDCQiAdwQCBoREf` | Thumbnail source only |
| 4 | `https://youtu.be/leOogJODD9s?si=3CVlFurH4PaJvYMs` | Used its own thumbnail |
| 5 | `https://youtu.be/7aMOurgDB-o?si=wzpfF57HOeK8H8fH` | Used its own thumbnail |
| 6 | `https://youtu.be/xC1cj9zhh6k?si=wNMueXQdDW0-nk7i` | Woh Din Lyrical - Chhichhore |
| 7 | `https://youtu.be/hoNb6HuNmU0?si=HE7-l4dNs_sMvi3s` | KHAIRIYAT (BONUS TRACK) - Chhichhore |
| 8 | `https://youtu.be/JeGBNhyJeE4?si=5KleQQis9lvpi3Kx` | Kal Ki Hi Baat Hai - Chhichhore |
| 9 | `https://youtu.be/nF5EVdpgLZE?si=mXGw2fJS7yrj2ePk` | CLIMA LINDO (SLOWED) |
| 10 | `https://youtu.be/M5OCLifZK1w?si=80VDI8PC2uZRf-p8` | Aarzu - trim end silence |
| 11 | `https://youtu.be/xvT1jH8B9AM?si=rEdpNUWXLNwD-2fk` | KALYANI - trim first 10s |
| 12 | `https://youtu.be/27QmkvKQLDk?si=3ColMxc0sAKgUymR` | Ada Bommale |
| 13 | `https://youtu.be/wuL1pvmtoSE?si=JUXKH8n1Qyuvl_Ad` | PLAY WITH FIRE (Phonk) |
| 14 | `https://youtu.be/tAcnQYvPl1s?si=exPkhhwpVZDRxJPW` | MONTAGEM ELDER (SUPER SLOWED) |
| 15 | `https://youtu.be/Sfv6OmOB1W4?si=XyE0Fp8I0cdtKp97` | ANDROMEDA - MONTAGEM COMA |
| 16 | `https://youtu.be/yxzHzspf3RU?si=Jj687Z1arkEBOVJV` | MONTAGEM CORAL |
| 17 | `https://youtu.be/EYaP4h6njtI?si=OYpv4tzp2TLey1st` | MONTAGEM TOMADA |
| 18 | `https://youtu.be/J1OumHmvtwY?si=HfrJ5QklGac8avD_` | Loser - Tame Impala |
| 19 | `https://youtu.be/Kw3935PH01E?si=vyW6NvMfd4Iir4qF` | UNAVAILABLE |

## Output Files (Session 2)

| # | File | Size | Title | Artist |
|---|------|------|-------|--------|
| 1 | `Phir Se - 8K Video ... -T-Series.mp3` | 4.5 MB | Phir Se - 8K Video \| Dhurandhar... | T-Series |
| 2 | `Rang De Lal (Oye Oye) (Audio) ... -T-Series.mp3` | 4.8 MB | Rang De Lal (Oye Oye) (Audio) \| ... | T-Series |
| 3 | `TERE ISHQ NE (Full Video) ... -T-Series.mp3` | 4.6 MB | TERE ISHQ NE (Full Video) \| ... | T-Series |
| 4 | `MC Lan e MC WM - Sua Amiga Vou Pegar (KondZilla) -Canal KondZilla.mp3` | 3.5 MB | MC Lan e MC WM - Sua Amiga Vou Pegar (KondZilla) | Canal KondZilla |
| 5 | `Bing Bing Boo (Lyrics) ... -THE DRAFT LYRICS.mp3` | 3.2 MB | Bing Bing Boo (Lyrics) - Yashraj... | THE DRAFT LYRICS |
| 6 | `Aa Seetadevi Navvula -Arijit Singh.mp3` | 4.3 MB | Aa Seetadevi Navvula | Arijit Singh |
| 7 | `Maanu, Annural Khalid - Jhol (Lyrics) -desibeats.mp3` | 4.6 MB | Maanu, Annural Khalid - Jhol (Lyrics) | desibeats |
| 8 | `Detective Conan Main Theme 🎷 Japanese Army Band -Jun-ichi Amano.mp3` | 3.6 MB | Detective Conan Main Theme 🎷 Japanese Army Band | Jun-ichi Amano |
| 9 | `Puttur Shree mahalingeshwara -Kadike Audio's.mp3` | 1.1 MB | Puttur Shree mahalingeshwara | Kadike Audio's |

## Output Files (Session 3)

| # | File | Size | Title | Artist |
|---|------|------|-------|--------|
| 1 | `DELTARUNE Chapter 2 OST - Ferris Wheel -0rionX99.mp3` | 1.1 MB | DELTARUNE Chapter 2 OST - Ferris Wheel | 0rionX99 |
| 10 | `DELTARUNE Chapter 2 OST - Ferris Wheel -0rionX99.mp3` | 1.1 MB | DELTARUNE Chapter 2 OST - Ferris Wheel | 0rionX99 |

## Output Files (Session 4)

| # | File | Size | Title | Artist |
|---|------|------|-------|--------|
| 1 | `Tokyo Ghoul Opening  -  'Unravel' by TK from Ling Toshite Sigure -Crunchyroll.mp3` | 1.8 MB | Tokyo Ghoul Opening \| "Unravel" by TK from Ling Toshite Sigure | Crunchyroll |

## Output Files (Session 5)

| # | File | Size | Title | Artist |
|---|------|------|-------|--------|
| 1 | `Demon Slayer - Opening 1 - 4K - 60FPS - Creditless -Anicrad.mp3` | 2.2 MB | Demon Slayer - Opening 1 \| 4K \| 60FPS \| Creditless \| | Anicrad |

Trimmed to 1:31 (91s).

## Output Files (Session 6)

| # | File | Size | Title | Artist |
|---|------|------|-------|--------|
| 1 | `Woh Din Lyrical -T-Series.mp3` | 6.6 MB | Woh Din Lyrical | T-Series |
| 2 | `KHAIRIYAT (BONUS TRACK) -T-Series.mp3` | 5.2 MB | KHAIRIYAT (BONUS TRACK) | T-Series |
| 3 | `Kal Ki Hi Baat Hai -T-Series.mp3` | 5.3 MB | Kal Ki Hi Baat Hai | T-Series |

## Output Files (Session 7)

| # | File | Size | Title | Artist |
|---|------|------|-------|--------|
| 1 | `CLIMA LINDO (SLOWED) -GANGSTER CLUB.mp3` | 1.8 MB | CLIMA LINDO (SLOWED) | GANGSTER CLUB |

## Output Files (Session 8)

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Noor, Khan, Madhurxo - Aarzu (Official Music Video) -Noor.mp3` | 3.98 MB | Noor, Khan, Madhurxo - Aarzu (Official Music Video) | Noor, Khan | Trimmed end silence (226s → 219s) |
| 2 | `KALYANI (with Shreya Ghoshal) -MONEY VERSE RECORDS.mp3` | 5.26 MB | KALYANI (with Shreya Ghoshal) OFFICIAL MUSIC VIDEO | MONEY VERSE RECORDS, ARJN | Trimmed first 10s (287s → 277s) |
| 3 | `Ada Bommale -Think Music India.mp3` | 4.17 MB | Ada Bommale - Video Song | Think Music India | |
| 4 | `PLAY WITH FIRE (Phonk) -Sky Bass.mp3` | 2.93 MB | ØMEN, PHXNTOM - PLAY WITH FIRE (Phonk) | Sky Bass | |
| 5 | `MONTAGEM ELDER (SUPER SLOWED) -Dj Samir.mp3` | 2.72 MB | MONTAGEM ELDER (SUPER SLOWED) | Dj Samir | |
| 6 | `ANDROMEDA - MONTAGEM COMA -elysian..mp3` | 2.62 MB | ANDROMEDA - MONTAGEM COMA | elysian. | |
| 7 | `MONTAGEM CORAL -DJ Holanda.mp3` | 3.61 MB | MONTAGEM CORAL (DJ HOLANDA, MC GW, MC TH & MC CYCLOPE) | DJ Holanda | |
| 8 | `MONTAGEM TOMADA -MXZI.mp3` | 2.71 MB | MONTAGEM TOMADA (Official Visualiser) | MXZI | |
| 9 | `Loser - Tame Impala (Spider-Man Brand New Day Soundtrack) -OfficialMovieSoundtrack.mp3` | 5.23 MB | Loser - Tame Impala (Spider-Man: Brand New Day Soundtrack) | OfficialMovieSoundtrack | |

Unavailable: `https://youtu.be/Kw3935PH01E` — "This video is not available"

## Output Files (Session 9)

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Free Bird -MOONLGHT.mp3` | 2.93 MB | Free Bird | MOONLGHT | 1:54, own thumbnail; tags cleaned (YouTube junk stripped) |

URL: `https://youtu.be/mQ1ycOl48Hc` — video title "Free Bird", uploader "MOONLGHT".

## Output Files (Session 10)

Batch of 27 URLs → 26 unique (duplicate `1ykU4QkchSE` deduped). All downloaded, thumbnail embedded, tags cleaned.

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Rama Rama -Rishab Rikhiram Sharma.mp3` | 7.88 MB | Rama Rama | Rishab Rikhiram Sharma | 6:35 |
| 2 | `Jatayu -Shreya Ghoshal.mp3` | 5.20 MB | Jatayu | Shreya Ghoshal | 4:43, Sk Records (tribute) |
| 3 | `Gal Sun -Sabat Batin.mp3` | 3.05 MB | Gal Sun | Sabat Batin | 2:59 |
| 4 | `Tum Hi Ho -Arijit Singh.mp3` | 3.89 MB | Tum Hi Ho | Arijit Singh | 4:10 |
| 5 | `Mann Mera -Gajendra Verma.mp3` | 4.23 MB | Mann Mera | Gajendra Verma | 3:48 |
| 6 | `TU -Talwiinder.mp3` | 2.91 MB | TU | Talwiinder | 2:12 |
| 7 | `Siya Ke Ram, Ram Ke Siya -Shreya Ghoshal.mp3` | 5.64 MB | Siya Ke Ram, Ram Ke Siya | Shreya Ghoshal | 4:49, Sk Records (tribute) |
| 8 | `Maan Meri Jaan -King.mp3` | 3.31 MB | Maan Meri Jaan | King | 3:15 |
| 9 | `Hamari Adhuri Kahani -Arijit Singh.mp3` | 6.51 MB | Hamari Adhuri Kahani | Arijit Singh | 6:39 |
| 10 | `Shree Hanuman Chalisa -Sukhwinder Singh.mp3` | 2.47 MB | Shree Hanuman Chalisa | Sukhwinder Singh | 1:49 |
| 11 | `Ramayana Rise of a Legend -T-Series.mp3` | 3.49 MB | Ramayana Rise of a Legend | T-Series | 2:23, **Trailer 2 (not a song)** |
| 12 | `Hookah Bar -Himesh Reshammiya.mp3` | 4.56 MB | Hookah Bar | Himesh Reshammiya | 4:14 |
| 13 | `Dharti Hai Ambar Hai -Hans Zimmer.mp3` | 4.04 MB | Dharti Hai Ambar Hai | Hans Zimmer | 2:24, fan-made interpretation (Rakri Music) |
| 14 | `Phir Bhi Tumko Chaahunga -Arijit Singh.mp3` | 5.05 MB | Phir Bhi Tumko Chaahunga | Arijit Singh | 5:58 |
| 15 | `Har Kisi Ko -Arijit Singh.mp3` | 5.34 MB | Har Kisi Ko | Arijit Singh | 5:33 |
| 16 | `Satyam Sanatanam -Subrata Poddar.mp3` | 5.65 MB | Satyam Sanatanam | Subrata Poddar | 4:44 |
| 17 | `Tu Jaane Na -Atif Aslam.mp3` | 6.02 MB | Tu Jaane Na | Atif Aslam | 5:37 |
| 18 | `Sitaare -Arijit Singh.mp3` | 3.94 MB | Sitaare | Arijit Singh | 4:03 |
| 19 | `Haseen -Talwiinder.mp3` | 3.35 MB | Haseen | Talwiinder | 3:25, acoustic version |
| 20 | `Rama Theme -Hans Zimmer.mp3` | 3.22 MB | Rama Theme | Hans Zimmer | 2:27, instrumental |
| 21 | `Vanvas -Shreya Ghoshal.mp3` | 4.25 MB | Vanvas | Shreya Ghoshal | 3:52, Sk Records (tribute) |
| 22 | `Ravana Tandav -Vishal Dadlani.mp3` | 2.95 MB | Ravana Tandav | Vishal Dadlani | 1:56 |
| 23 | `Ram Ka Sandesh -Shreya Ghoshal.mp3` | 5.16 MB | Ram Ka Sandesh | Shreya Ghoshal | 4:45, Sk Records (tribute) |
| 24 | `Jai Jai Ram -Shreya Ghoshal.mp3` | 3.62 MB | Jai Jai Ram | Shreya Ghoshal | 2:08 |
| 25 | `Sita's Aspiration -A.R. Ameen.mp3` | 3.69 MB | Sita's Aspiration | A.R. Ameen | 2:42 |
| 26 | `Mangal Rang -Arijit Singh.mp3` | 3.54 MB | Mangal Rang | Arijit Singh | 2:25 |

All Ramayana tracks tagged `album=Ramayana`; others `album=<song title>`. Genre `Music`, `date` = upload year.

## Output Files (Session 11)

35 URLs given → 34 downloaded. `mQ1ycOl48Hc` (Free Bird) now returns "Video unavailable"; already have it from Session 9. All files: cover embedded, tags cleaned (`album=<title>`, genre `Music`, date = upload year).

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Aasa Pulla -G.V. Prakash Kumar.mp3` | 3.12 MB | Aasa Pulla | G.V. Prakash Kumar | dup of `Hindi/` |
| 2 | `Kokki -Anirudh Ravichander.mp3` | 5.26 MB | Kokki | Anirudh Ravichander | dup of `Hindi/` |
| 3 | `Ride It -DUORUSH.mp3` | 5.61 MB | Ride It | DUORUSH | dup of `New/` |
| 4 | `Circle -Netrum.mp3` | 4.67 MB | Circle | Netrum | |
| 5 | `Where We Started -Lost Sky.mp3` | 4.17 MB | Where We Started | Lost Sky | |
| 6 | `Pardesiya -Sonu Nigam.mp3` | 4.75 MB | Pardesiya | Sonu Nigam | |
| 7 | `Chuttamalle -Shilpa Rao.mp3` | 4.60 MB | Chuttamalle | Shilpa Rao | |
| 8 | `Kalank -Arijit Singh.mp3` | 5.73 MB | Kalank | Arijit Singh | |
| 9 | `Baby -Justin Bieber.mp3` | 3.73 MB | Baby | Justin Bieber | |
| 10 | `Cupid -FIFTY FIFTY.mp3` | 17.30 MB | Cupid | FIFTY FIFTY | 19:10 looped lyric video |
| 11 | `Shinunoga E-Wa -Fujii Kaze.mp3` | 1.99 MB | Shinunoga E-Wa | Fujii Kaze | |
| 12 | `Racing Into The Night -YOASOBI.mp3` | 4.31 MB | Racing Into The Night | YOASOBI | |
| 13 | `Blue -Yung Kai.mp3` | 17.32 MB | Blue | Yung Kai | 19:41 looped lyric video; dup of `Music/` |
| 14 | `Pastlives -sapientdream.mp3` | 2.96 MB | Pastlives | sapientdream | |
| 15 | `Mary On A Cross -Ghost.mp3` | 4.23 MB | Mary On A Cross | Ghost | |
| 16 | `Mockingbird -Eminem.mp3` | 4.48 MB | Mockingbird | Eminem | |
| 17 | `Bloody Mary -Lady Gaga.mp3` | 4.14 MB | Bloody Mary | Lady Gaga | |
| 18 | `Happy Nation -Ace of Base.mp3` | 3.67 MB | Happy Nation | Ace of Base | |
| 19 | `Gangsta's Paradise -Coolio.mp3` | 4.02 MB | Gangsta's Paradise | Coolio | |
| 20 | `All Falls Down -Alan Walker.mp3` | 3.54 MB | All Falls Down | Alan Walker | |
| 21 | `Payphone -Maroon 5.mp3` | 3.71 MB | Payphone | Maroon 5 | |
| 22 | `The Lazy Song -Bruno Mars.mp3` | 3.03 MB | The Lazy Song | Bruno Mars | |
| 23 | `Life Goes On -Oliver Tree.mp3` | 3.82 MB | Life Goes On | Oliver Tree | |
| 24 | `My Ordinary Life -The Living Tombstone.mp3` | 4.66 MB | My Ordinary Life | The Living Tombstone | |
| 25 | `World's Smallest Violin -AJR.mp3` | 3.53 MB | World's Smallest Violin | AJR | |
| 26 | `Another Love -Tom Odell.mp3` | 4.23 MB | Another Love | Tom Odell | dup of `Music/` |
| 27 | `Dusk Till Dawn -ZAYN.mp3` | 5.19 MB | Dusk Till Dawn | ZAYN | |
| 28 | `Snowman -Sia.mp3` | 3.35 MB | Snowman | Sia | |
| 29 | `Enemy -Imagine Dragons.mp3` | 3.76 MB | Enemy | Imagine Dragons | |
| 30 | `STAY -The Kid LAROI.mp3` | 2.79 MB | STAY | The Kid LAROI | |
| 31 | `Loser -Tame Impala.mp3` | 4.68 MB | Loser | Tame Impala | dup of `Music/Loser - Tame Impala.mp3` |
| 32 | `Heathens -Twenty One Pilots.mp3` | 3.98 MB | Heathens | Twenty One Pilots | |
| 33 | `Stressed Out -Twenty One Pilots.mp3` | 4.15 MB | Stressed Out | Twenty One Pilots | |
| 34 | `Waiting For Love -Avicii.mp3` | 4.14 MB | Waiting For Love | Avicii | |

Unavailable: `mQ1ycOl48Hc` — "Video unavailable" (Free Bird; already downloaded in Session 9).

## Output Files (Session 12)

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Nadaaniyan -Akshath.mp3` | 2.87 MB | Nadaaniyan | Akshath | 2:49 |
| 2 | `Chammak Challo -Akon.mp3` | 4.92 MB | Chammak Challo | Akon | 4:06, Ra.One |
| 3 | `Pardesiya (Song Version) -Sonu Nigam.mp3` | 3.64 MB | Pardesiya (Song Version) | Sonu Nigam | 2:58; kept alongside the 3:54 film version from Session 11 |

Source: `N4wK3NtVRT0` (Pardesiya song version), `HeBJMzrM7hU` (Nadaaniyan), `oAVhUAaVCVQ` (Chammak Challo).

## Output Files (Session 13)

17 URLs → 16 downloaded; `fLexgOxsZu0` (The Lazy Song) skipped as already downloaded in Session 11. `Blue` replaced the 19:41 looped lyric version from Session 11 with the 3:34 original.

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Swami Pardesh -Suraj Tratak.mp3` | 3.41 MB | Swami Pardesh | Suraj Tratak | 2:55 |
| 2 | `Dil Lagana Mana Tha -Krish.mp3` | 3.94 MB | Dil Lagana Mana Tha | Krish | 3:25 |
| 3 | `Espresso -Sabrina Carpenter.mp3` | 3.01 MB | Espresso | Sabrina Carpenter | 2:54 |
| 4 | `NIGHT DANCER -imase.mp3` | 3.65 MB | NIGHT DANCER | imase | 3:31 |
| 5 | `Blue -Yung Kai.mp3` | 3.88 MB | Blue | Yung Kai | 3:34 (replaced 19:41 loop) |
| 6 | `Wrap Me In Plastic -MOMOLAND.mp3` | 3.90 MB | Wrap Me In Plastic | MOMOLAND | 3:15 |
| 7 | `En Malare -madrascala.mp3` | 4.35 MB | En Malare | madrascala | 3:56 |
| 8 | `Nadiyondu -Siddhartha Belmannu.mp3` | 4.38 MB | Nadiyondu | Siddhartha Belmannu | 4:32 |
| 9 | `Menake -Tanmay Gururaj.mp3` | 4.81 MB | Menake | Tanmay Gururaj | 3:27 |
| 10 | `Kiliye Kiliye -S. Janaki.mp3` | 2.55 MB | Kiliye Kiliye | S. Janaki | 2:05 |
| 11 | `Sunroof -Nicky Youre.mp3` | 3.51 MB | Sunroof | Nicky Youre | 2:55 |
| 12 | `Jenina Goodu Naavella -Rajesh Krishnan.mp3` | 3.83 MB | Jenina Goodu Naavella | Rajesh Krishnan | 5:24 |
| 13 | `Kaise Batabu -Sadri Vibe.mp3` | 4.91 MB | Kaise Batabu | Sadri Vibe | 3:58, AI vocals |
| 14 | `Hay Re Tor Bina -Skindo.mp3` | 3.62 MB | Hay Re Tor Bina | Skindo | 3:16, AI vocals |
| 15 | `Dheem Ta Dare -Anandalaya.mp3` | 2.00 MB | Dheem Ta Dare | Anandalaya | 2:55 |
| 16 | `Har Kisike Dil Me Ek Ladki Ka Khayal Rehta Hai -Alka Yagnik.mp3` | 6.62 MB | Har Kisike Dil Me Ek Ladki Ka Khayal Rehta Hai | Alka Yagnik | 5:49 |

## Output Files (Session 14)

| # | File | Size | Title | Artist | Notes |
|---|------|------|-------|--------|-------|
| 1 | `Cupid -FIFTY FIFTY.mp3` | 3.44 MB | Cupid | FIFTY FIFTY | 3:23; replaced the 19:10 looped lyric version from Session 11 |

Source: `Qc7_zRjH808` — official MV, uploaded 2023.






## Output Files

### File 1: `Lastraveler - Bliss -Lastraveler.mp3`
- **Size:** 3,598,204 bytes
- **Title:** Lastraveler | Bliss
- **Artist:** Lastraveler
- **Thumbnail:** From its own video (embedded as PNG)
- **Duration:** 2:41

### File 2: `YOASOBI「アイドル」 Official Music Video -YOASOBI.mp3`
- **Size:** 3,757,991 bytes
- **Title:** YOASOBI「アイドル」 Official Music Video
- **Artist:** YOASOBI
- **Thumbnail:** From `https://youtu.be/PgBvV9ofjmA` (embedded as JPEG)
- **Duration:** 3:45

### File 3: `Tokyo Ghoul Opening  -  'Unravel' by TK from Ling Toshite Sigure -Crunchyroll.mp3`
- **Size:** 1,868,839 bytes
- **Title:** Tokyo Ghoul Opening | "Unravel" by TK from Ling Toshite Sigure
- **Artist:** Crunchyroll
- **Thumbnail:** From its own video (embedded as PNG)
- **Duration:** 1:32

## Naming Convention
Format: `{MusicName} -{Artist}.mp3`
- Space before the dash, no space after (e.g. `Night Changes -One Direction.mp3`)
- **MusicName**: just the song title. Do NOT include descriptors like `(Lyrics)`, `(Lyric video)`, `(Official Video)`, `(Music Video)`, `(Video Song)`, `(Instrumental)`, `(Slowed)`, `(Audio)`, season/show names, channel tags, or sequel suffixes.
- **Artist**: only ONE main artist (e.g. `No Lie -Sean Paul` not `Sean Paul, Dua Lipa`; featured artists are dropped).
- Remove all pipe/`|`/`~`/`×` separators from the song title.
- The metadata must match: `title` = MusicName, `artist` = Artist.
- NOTE: `--add-metadata` sets `title` to the raw video title and `artist` to the uploader channel, NOT the cleaned name. After downloading, fix metadata with ffmpeg (see "Set/fix metadata") so it matches the filename.
- Song title stays in its original language (e.g. `DŽANUM`, `꽃`), but Romanized titles are also acceptable.

## Key Commands Used

### Update yt-dlp
```bash
# Installed via pacman on CachyOS
sudo pacman -Syu yt-dlp
```

### Get video info
```bash
yt-dlp --print "%(title)s|%(uploader)s|%(id)s" <URL>
```

### Download with own thumbnail
```bash
yt-dlp -x --audio-format mp3 --embed-thumbnail --add-metadata \
    -o "<filename>.%(ext)s" <URL>
```

### Download with own thumbnail (default client, no deno needed)
```bash
yt-dlp -x --audio-format mp3 --embed-thumbnail --add-metadata \
    -o "<filename>.%(ext)s" <URL>
```
System `yt-dlp` (2026.10.21) handles JS challenges natively — no deno needed.

### Download with web_music player client (for 403 issues)
```bash
yt-dlp --extractor-args "youtube:player_client=web_music" \
    -x --audio-format mp3 --embed-thumbnail --add-metadata \
    -o "<filename>.%(ext)s" <URL>
```
NOTE: web_music client now requires a GVS PO Token (https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide) and fails without it. Prefer the default client.

### Detect silence in audio
```bash
ffmpeg -i "<input.mp3>" -af silencedetect=n=-40dB:d=0.5 -f null - 2>&1 | grep silence_
```

### Trim audio to specific duration
```bash
ffmpeg -y -i "<input.mp3>" -t <seconds> -c copy -map_metadata 0 -id3v2_version 3 "<output.mp3>"
```

### Trim audio starting from specific time
```bash
ffmpeg -y -ss <seconds> -i "<input.mp3>" -c copy -map_metadata 0 -id3v2_version 3 "<output.mp3>"
```

### Download external thumbnail only
```bash
yt-dlp --skip-download --write-thumbnail --convert-thumbnails jpg \
    -o "<output_name>" <URL>
```

### Attach external thumbnail to MP3
```bash
ffmpeg -i "<audio.mp3>" -i "<thumbnail.jpg>" -map 0:0 -map 1:0 -c copy \
    -id3v2_version 3 -metadata:s:v title="Album cover" \
    -metadata:s:v comment="Cover (front)" "<output.mp3>"
```

### Set/fix metadata
```bash
ffmpeg -i "<input.mp3>" -i "<input.mp3>" -map 0 -c copy \
    -metadata title="<title>" -metadata artist="<artist>" \
    -id3v2_version 3 "<output.mp3>"
```

### Clean tags (strip YouTube junk, keep cover)
```bash
ffmpeg -y -i "<input.mp3>" -map 0:a -map 0:v -c copy -map_metadata -1 \
    -id3v2_version 3 \
    -metadata title="<title>" -metadata artist="<artist>" \
    -metadata album="<album>" -metadata genre="Music" -metadata date="<year>" \
    -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" \
    "<output.mp3>"
```
Removes `description`, `synopsis`, `purl`, `comment` URL added by `--add-metadata`, keeps audio + embedded cover.

## Issues Encountered
0. **deno no longer needed** — System `yt-dlp` 2026.10.21 solves JS challenges natively; default player client works out of the box. The `web_music` client now needs a GVS PO Token and is unreliable — use the default client instead.
1. **yt-dlp too old** — (Old OS) System package was 2024.04.09, needed 2026.06.09. Downloaded binary to `~/.local/bin/`. Now using pacman package on CachyOS.
2. **No JS runtime** — yt-dlp warned about missing Deno/JS runtime; extraction still worked.
3. **Pipe `|` invalid in filenames** — Filesystem doesn't allow `|` character; replaced with ` - `.
4. **`--parse-metadata` not setting artist correctly** — yt-dlp's `--parse-metadata "artist:%(uploader)s"` failed silently (set artist to "NA"). Used ffmpeg to set metadata afterward instead.
5. **Pipe in title breaks `--print` field parsing** — Using `--print "%(title)s|%(uploader)s"` when title contains `|` causes wrong field extraction. Title might be: `"A | B | C"` with uploader `"X"`, parsed as title="A", uploader="B". Fixed by using `--dump-json` and parsing with Python/JSON.
6. **HTTP 403 errors on some formats** — Some videos returned 403 errors when downloading webm format 251. Fixed by trying m4a format 140 instead.
7. **HTTP 403 on all audio formats (android_vr client)** — In session 8, both webm 251 and m4a 140 returned 403. Root cause: missing JS runtime for signature solving. Fixed by installing deno (`~/.deno/bin/deno`).
8. **android_vr client still 403 after deno install** — Even with deno available, the android_vr player client URLs returned 403 on download. Fixed by using `--extractor-args "youtube:player_client=web_music"` which downloads format 18 (360p mp4 with audio) and converts to mp3.
9. **`silenceremove` ffmpeg filter too aggressive** — Using `silenceremove` with default params on Aarzu produced a 0.6s file from a 226s song. Fixed by using `silencedetect` to find silence boundaries, then trimming with `-t` to the last non-silence point.
10. **ffmpeg cannot edit files in-place** — `ffmpeg -i input.mp3 ... -o input.mp3` fails. Must use a temp file then `mv`.

## Current Directory
`/home/bluepick/Music/AddCover/`

## Session 9 Verification (CachyOS)
- `yt-dlp` → `/usr/bin/yt-dlp` 2026.10.21 (pacman)
- `ffmpeg` → `/usr/bin/ffmpeg` n9.0.2, `lame` → `/usr/bin/lame`
- Tested full pipeline on `https://youtu.be/iKnqjtLeWmg` with `--download-sections "*0-8"`:
  - metadata print OK, audio download OK (no 403), mp3 conversion OK, thumbnail embed OK, ID3 title/artist OK.
- Working dir now `/home/bluepick/Music/AddCover/` (old `~/Audio/AddCover/` is gone).
