# AI Multilingual Video Dubbing Pipeline

## Overview

This project is an end-to-end AI-powered multilingual video dubbing pipeline that automatically converts English videos into multiple Indian languages.

The pipeline performs:

* Audio extraction from video
* Speech-to-text transcription using WhisperX
* Translation into 8 Indian languages
* Text-to-speech generation
* Audio-video synchronization
* Automatic dubbed video generation

## Supported Languages

* Hindi
* Telugu
* Tamil
* Bengali
* Marathi
* Gujarati
* Kannada
* Malayalam

## Tech Stack

* Python
* WhisperX
* FFmpeg
* gTTS
* Pydub
* Deep Translator

## Features

* Automated speech recognition
* Multilingual translation
* Speech synthesis
* Audio synchronization
* End-to-end pipeline automation
* One-command execution

## Testing and Results

The pipeline was tested on 3 different English-language videos.

For each video:

* Audio was extracted automatically
* Speech was transcribed using WhisperX
* Content was translated into 8 Indian languages
* TTS audio was generated
* Dubbed videos were created with synchronized audio

### Output Generated

* 3 Input Videos
* 8 Languages per Video
* 24 Dubbed Videos Generated

## Usage

Run:

python run_pipeline.py

or

python run_all.py

## Author

Swatti Suchi
