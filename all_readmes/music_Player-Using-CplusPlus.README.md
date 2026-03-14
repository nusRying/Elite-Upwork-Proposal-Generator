name:	nusRying/music_Player-Using-CplusPlus
description:	
--
# Music Player README

This is a simple command-line music player program implemented in C++. The program allows you to create playlists, add songs to playlists, shuffle playlists, play audio files (WAV, MP3, etc.), search for songs in a playlist, and more. It supports two versions, each with its own set of features.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Usage](#usage)
4. [Getting Started](#getting-started)
5. [Version Selection](#version-selection)
6. [Storage Type](#storage-type)
7. [Songs List](#songs-list)
8. [Credits](#credits)
9. [Important Notes](#important-notes)
10. [GitHub Repository](#github-repository)

## Introduction <a name="introduction"></a>

This music player program provides a simple command-line interface to manage playlists, add and play songs, shuffle playlists, and more. It offers two versions, each with its own features. The program utilizes the Windows API for audio playback and file management.

## Features <a name="features"></a>

- Create new playlists.
- Add songs to playlists.
- Shuffle playlist order.
- Play audio files (WAV, MP3, etc.).
- Pause, resume, and close audio playback.
- Search for songs in a playlist.
- Remove songs from a playlist.
- Display developer and program information.

## Usage <a name="usage"></a>

The program operates via a command-line interface. It provides options to create and manage playlists, add songs, play audio files, and more. The user is presented with a menu-driven interface to interact with the features.

## Getting Started <a name="getting-started"></a>

1. Clone or download the repository from [GitHub](https://github.com/nusRying/music_Player-Using-CplusPlus).
2. Open a terminal or command prompt.
3. Navigate to the directory where the code is located.
4. Compile the code using a C++ compiler (e.g., g++).
   ```
   g++ -o music_player.exe main.cpp -lwinmm
   ```
5. Run the compiled executable:
   ```
   music_player.exe
   ```

## Version Selection <a name="version-selection"></a>

Upon launching the program, you will be prompted to choose between two available versions: version 1 and version 2. Select the desired version to proceed.

## Storage Type <a name="storage-type"></a>

After selecting a version, you can choose the storage type you are using (CD or USB). This selection determines the source of the audio files for playback.

## Songs List <a name="songs-list"></a>

The program will display a list of available songs based on the selected storage type. You can enter the number of the song you want to play, and the program will play the selected audio file. During playback, you can control the playback using specific keys (see [Important Notes](#important-notes)).

## Credits <a name="credits"></a>

The program offers a "Credits" option where you can find information about the developer, institution, and ways to access the source code (GitHub repository, LinkedIn profile, etc.).

## Important Notes <a name="important-notes"></a>

- Press 'p' to pause the audio playback.
- Press 'r' to resume the audio playback.
- Press 'e' to close the audio playback.
- Press 'l' to go back to the songs list.

**Note:** It's important to close the playing audio before opening a new song to avoid issues.

## GitHub Repository <a name="github-repository"></a>

For access to the source code and updates, visit the [GitHub repository](https://github.com/nusRying/music_Player-Using-CplusPlus).

This program was developed by Umair Ejaz as part of a project at NUST CEME. For more information or inquiries, you can contact the developer on LinkedIn: [Umair Ejaz](https://www.linkedin.com/in/umair-ejaz/)

