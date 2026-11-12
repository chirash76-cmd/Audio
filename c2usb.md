# Car USB Music Organizer

## Default Paths
- Source: `/home/bluepick/FileSystem/01-ThisPC/Audio`
- Destination: `/run/media/bluepick/Music-Car`

## Copy Rules (FAT32 creation-order based)

### Playback Order
1. `New/` — directory created first (plays first)
   - All songs in case-insensitive alphabetical order
   - Any number-starting songs at the end
2. `Animated/` — directory created second (plays second)
   - All songs in case-insensitive alphabetical order
   - Any number-starting songs at the end
   - `BlackPink/` subfolder created last, after all songs (plays at the end of Animated)
3. `Music/` — directory created third (plays third)
   - All songs in case-insensitive alphabetical order
   - Any number-starting songs at the end
4. `Hindi/` — directory created fourth (plays fourth)
   - All songs in case-insensitive alphabetical order
5. `Phonk/` — directory created fifth (plays fifth)
   - All songs in case-insensitive alphabetical order
6. `Football/` — directory created sixth (plays sixth)
   - All songs in case-insensitive alphabetical order
7. `OldClassic/` — directory created seventh (plays seventh)
   - All songs in case-insensitive alphabetical order
8. `Rap/` — directory created eighth (plays eighth)
   - All songs in case-insensitive alphabetical order
9. `Remix/` — directory created ninth (plays ninth)
   - All songs in case-insensitive alphabetical order
10. `UNP/` — directory created tenth (plays tenth)
   - All songs in case-insensitive alphabetical order

### Notes
- `AddCover/` is NOT copied (no audio files)
- Each folder's contents: case-insensitive alphabetical order, number-starting at end

### Important Behavior
- Do NOT rename any files or folders
- Order is controlled by FAT32 directory entry creation sequence
- Clear the destination entirely before copying
- Copy in the exact sequence above

## Usage
- When user says: `copy to usb` — execute the full copy using the rules above
- When user says: `copy to usb <additional args>` — apply any modifications specified while keeping these rules as the base
