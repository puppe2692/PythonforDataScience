import sys
import time
import shutil

def format_time(seconds):
	# Convert seconds to hours, minutes, and seconds
	m, s = divmod(seconds, 60)
	return f"{int(m):02d}:{int(s):02d}"

def ft_tqdm(lst: range) -> None:
	total = len(lst)
	terminal_size = shutil.get_terminal_size()
	length = (terminal_size.columns) / 1.3
	start_time = time.time()
	progress_format = "{percentage:3.0f}%|{bar}| {item:3}/{total} [{etime}<{rtime}, {iter:3.2f}it/s]    "

	for i, item in enumerate(lst):
		percentage = i / total * 100
		bar_length = int((int(length) + 1) * (i / total))
		bar = "\u2588" * bar_length + " " * (int(length) - bar_length)

		iter_rate = (i + 1) / (time.time() - start_time)
		elapsed_time = time.time() - start_time

		if i > 0:
			rtime = format_time((elapsed_time / i) * (total - i))
		else:
			rtime = format_time(time.time() - time.time())

		etime = format_time(elapsed_time)

		sys.stdout.write("\r" + progress_format.format(total=total,item=item + 1, bar=bar, percentage=percentage, rtime=rtime, etime=etime, iter=iter_rate))
		sys.stdout.flush()
		yield item
	
	sys.stdout.write('\n')