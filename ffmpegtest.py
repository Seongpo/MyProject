import ffmpeg
stream = ffmpeg.input('./image/SampleVideo_1280x720_1mb.mp4')
stream = ffmpeg.hflip(stream)
# stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)