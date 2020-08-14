PYTHON = python3
SOURCES = server.py
LOG = server.log

run: 
	nohup ${PYTHON} -u ${SOURCES} >> ${LOG} 2>&1 & echo $$! > server.PID 

kill: 
	kill `cat server.PID` || true

clean:
	rm ${LOG} || true
	rm *.PID