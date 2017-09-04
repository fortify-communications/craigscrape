#!/bin/sh

out=`/usr/bin/sqlite3 bmw.db  "select * from posts where strftime(posted_at) > datetime('now', '-1 day') and email_sent = 0;"`


if [ -n "$out" ]; then
  echo $out | mail -s "carpurchase bmw" andrei@odeski.ca

  # mark in db as sent
  /usr/bin/sqlite3 bmw.db "update posts set email_sent=1;"
fi

