import glob, os, shutil

SQL_BACKUP_FOLDER = r'\\ua-db01\d$\Microsoft SQL Server\Backup'
FS_BACKUP_FOLDER = r'E:\STORAGE\DB01\Backups'
BACKUP_FILENAME = r'db-top-1_backup*.bak'
with open('move_backups.log', 'a') as log_file:
    # Check free space
    total, used, free = shutil.disk_usage(FS_BACKUP_FOLDER)
    log_file.write('Used space: ' + str(used*100//total) + '%\n')
    if used*100//total > 70:
        fs_files = glob.glob(os.path.join(FS_BACKUP_FOLDER, BACKUP_FILENAME))
        if fs_files:
            log_file.write('Remove file: ' + min(fs_files) + '\n')
            os.remove(min(fs_files))

    db_files = glob.glob(os.path.join(SQL_BACKUP_FOLDER, BACKUP_FILENAME))
    #print('db_files: ', db_files, '\n')
    log_file.write('Move file: ' + min(db_files) + '\n')
    shutil.move(min(db_files), FS_BACKUP_FOLDER)
