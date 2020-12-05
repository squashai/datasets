SquashAI Datasets
=================

This repository contains a collection of datasets and helper scripts
related to the [SquashAI Project](https://squashai.github.io).

A summary of the data contained in the datasets is available
[here](https://squashai.github.io/#/data).

## Dataset Details

### T-box Keypoints

File: `tboxes.csv`

Coordinates of the four corners of the box enclosing the T-area,
represented in the same coordinate space of the referenced image.

![T-box Points](https://user-images.githubusercontent.com/13051155/100998804-42dd6100-355c-11eb-9859-6d52399ee092.png)

### Player Bounding Boxes

File: `pboxes.csv`

Bounding boxes of the players, represented as width, height and center
coordinates, in the same coordinate space of the referenced image.

![Player Bounding Boxes](https://user-images.githubusercontent.com/13051155/101011845-006b5280-3563-11eb-97b1-679cd56c8fae.png)

### Transposed Player Positions and General Attributes

Files: `positions.csv`, `attributes.csv`, `*.json`

General information (player names, shirt color, _replay_ and _action_
tags) and coordinates of the player positions on the squash court,
represented on a _(-3.2, 3.2)x(-4.875, 4.875)_ coordinate space. The
_csv_ files contain information extracted from the _json_ files. The
_json_ files were created with the [SquashAI
Editor](https://squashai.github.io/#/editor).

![Transposed Player Positions](https://user-images.githubusercontent.com/13051155/100998836-4c66c900-355c-11eb-9cc4-dc4f99ffa0a8.png)

## Scripts

 * `scripts/build.py`: download the video files and extracts the
   images the datasets refer to. The video and image files will be
   stored in `media/`

 * `scripts/json2csv.py`: extracts information from the _json_
   datasets into _csv_ files

 * `scripts/dist.py`: create a _tar.gz_ archive with metadata and raw
   image files