def transcribe_gcs_with_word_time_offsets(gcs_uri):
	import io
	from google.cloud import speech
	from google.cloud.speech import enums
	from google.cloud.speech import types
	client = speech.SpeechClient()

	audio = types.RecognitionAudio(uri=gcs_uri)
	config = types.RecognitionConfig(
			encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
			sample_rate_hertz=16000, #16000 for flac, 8000 for wav
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
transcribe_gcs_with_word_time_offsets("gs://cloud-samples-tests/speech/brooklyn.flac")
