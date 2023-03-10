import gr4vy_3ds_transaction_report

if __name__ == '__main__':
    gr4vy_id = input('Enter Gr4vy Instance ID: ')
    environment = input('Enter environment (sandbox or production): ')
    private_key = input('Enter private key file name: ')
    log_file = input('Enter log file: ')
    output_file = input('Enter ouput file name: ')
    gr4vy_3ds_transaction_report.run_report(gr4vy_id, environment, private_key, log_file, output_file)
