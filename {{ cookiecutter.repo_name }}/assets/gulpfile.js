var gulp = require('gulp'),
    concat = require('gulp-concat'),
    addsrc = require('gulp-add-src'),
    notify = require('gulp-notify'),

    compass = require('gulp-compass'),
    autoprefixer = require('gulp-autoprefixer'),

    minifycss = require('gulp-minify-css'),

    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),

    runSequence = require('run-sequence'),
    livereload = require('gulp-livereload');

// Compass
gulp.task('compass', function() {
  return gulp.src('/gulp/sass/style.scss')
    .pipe(compass({
      comments: true,
      css: '/gulp/css/dev',
      require: ['compass/import-once/activate', 'breakpoint']
    }))
    .on('error', function (err) {
      this.emit('end');
    })
    .pipe(autoprefixer('last 2 version'))
    .pipe(gulp.dest('/gulp/css/dev'))
    .pipe(notify({message: 'Compass build task complete'}));
});

// Build CSS
gulp.task('build_css', function() {
  return gulp.src(['/gulp/css/dev/lib/*.css', '/gulp/css/dev/style.css'])
    .pipe(concat('style.min.css'))
    .pipe(minifycss({
      keepSpecialComments: 0
    }))
    .pipe(gulp.dest('/gulp/css/build'))
    .pipe(notify({message: 'CSS build task complete'}));
});

// Build JS
gulp.task('build_js', function() {
   return gulp.src('/gulp/js/dev/*.js')
    .pipe(jshint())
    .pipe(jshint.reporter('jshint-stylish'))
    .pipe(concat('main.js'))
    .pipe(uglify({
      compress: {
        drop_console: true
      }
    }))
    .pipe(addsrc.prepend(['/gulp/js/dev/lib/*.js', '!/gulp/js/dev/lib/jquery.min.js']))
    .pipe(addsrc.prepend('/gulp/js/dev/lib/jquery.min.js'))
    .pipe(concat('main.min.js'))
    .pipe(uglify({
      compress: false,
      mangle: false
    }))
    .pipe(gulp.dest('/gulp/js/build'))
    .pipe(notify({message: 'JS build task complete'}));
});

// Watch
gulp.task('watch', function() {
  livereload.listen();

  gulp.watch(['/gulp/js/dev/*.js', '/gulp/js/dev/lib/*.js'], ['build_js']);
  gulp.watch(['/gulp/sass/*.scss', '/gulp/css/dev/lib/*.css'], function() {
   runSequence('compass', 'build_css');
  })

  gulp.watch(['/gulp/css/dev/style.css', '/gulp/css/dev/lib/*.css']).on('change', livereload.changed);
});

// Default
gulp.task('default', function() {
  runSequence(['compass', 'build_js'], 'build_css', 'watch');
});
