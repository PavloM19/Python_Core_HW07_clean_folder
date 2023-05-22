# File_sorting
A program for sorting files by type in a given folder

The program works with the following file types and formats:

images = ('jpeg', 'png', 'jpg', 'svg')

video = ('avi', 'mp4', 'mov', 'mkv')

docs = ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx')

music = ('mp3', 'ogg', 'wav', 'amr')

archives = ('zip', 'gz', 'tar', 'rar', '7z')

The program sorts the following file types into the appropriate folders.
At the same time the tar and zip archives are additionally unpacked to the folder with the file name.
Files with an unknown extension are moved to the folder with the name "other".
