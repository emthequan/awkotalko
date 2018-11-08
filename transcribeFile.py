def transcribe_file(speech_file):
	import io
	"""Transcribe the given audio file."""
	from google.cloud import speech
	from google.cloud.speech import enums
	from google.cloud.speech import types
	client = speech.SpeechClient()
	with io.open(speech_file, 'rb') as audio_file:
		content = audio_file.read()

	audio = types.RecognitionAudio(content=content)
	config = types.RecognitionConfig(
			encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
			sample_rate_hertz=8000,
			language_code='en-US')

	response = client.recognize(config, audio)
	# Each result is for a consecutive portion of the audio. Iterate through
	# them to get the transcripts for the entire audio file.
	for result in response.results:
		# The first alternative is the most likely one for this portion.
		print(u'Transcript: {}'.format(result.alternatives[0].transcript))
def transcribe_gcs_with_word_time_offsets(gcs_uri):
	"""Transcribe the given audio file asynchronously and output the word time
	offsets."""
	from google.cloud import speech
	from google.cloud.speech import enums
	from google.cloud.speech import types
	import io
	client = speech.SpeechClient()

	audio = types.RecognitionAudio(uri=gcs_uri)
	config = types.RecognitionConfig(
			encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
			sample_rate_hertz=8000,
			language_code='en-US',
			enable_word_time_offsets=True)

	operation = client.long_running_recognize(config, audio)

	print('Waiting for operation to complete...')
	result = operation.result(timeout=90)

	for result in result.results:
			alternative = result.alternatives[0]
			print(u'Transcript: {}'.format(alternative.transcript))
			print('Confidence: {}'.format(alternative.confidence))

			for word_info in alternative.words:
					word = word_info.word
					start_time = word_info.start_time
					end_time = word_info.end_time
					print('Word: {}, start_time: {}, end_time: {}'.format(
							word,
							start_time.seconds + start_time.nanos * 1e-9,
							end_time.seconds + end_time.nanos * 1e-9))
transcribe_file("eng_m1.wav")
#transcribe_gcs_with_word_time_offsets("eng_m1.wav")

