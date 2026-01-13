#!/bin/bash

BASE="media/base.mp4"
VIDEOS=(media/video1.mp4 media/video2.mp4 media/video3.mp4)

TRANSITION="fade"
DURATION=1
OFFSET=0

mkdir -p media/transitions

for V in "${VIDEOS[@]}"; do
  NAME=$(basename "$V" .mp4)

  echo "Creating base -> $NAME"
  ffmpeg -y -i "$BASE" -i "$V" \
    -filter_complex "xfade=transition=$TRANSITION:duration=$DURATION:offset=$OFFSET" \
    "media/transitions/base_to_$NAME.mp4"

  echo "Creating $NAME -> base"
  ffmpeg -y -i "$V" -i "$BASE" \
    -filter_complex "xfade=transition=$TRANSITION:duration=$DURATION:offset=$OFFSET" \
    "media/transitions/${NAME}_to_base.mp4"
done

echo "DONE"
