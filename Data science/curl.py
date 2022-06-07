import subprocess

start = 2000001
end   = 2000005
with open("data.txt", "w") as file:
    for sbd in range(start, end):
        command = 'curl -F "sobaodanh=0' + str(sbd) + '" diemthi.hcm.edu.vn/Home/Show'
        result =  subprocess.check_output(command)
        file.write(str(result) + "\n")